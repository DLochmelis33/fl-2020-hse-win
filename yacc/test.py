from parser import parser


def f(text):
    try:
        parser.parse(text)
    except SyntaxError:
        return False
    else:
        return True


def test_old_basic():
    # assert f('')
    assert f('a.')
    assert f('xy_z .')
    assert not f('a')
    assert not f('.')
    assert f('\t\taa\n  \t.\n')
    assert not f('&')
    assert not f('WOW = 10')


def test_old_corkscrew():
    assert f('a:-b.')
    assert f('ababa :- \t babab    \n\t\n .')
    assert not f('a :- :- .')
    assert not f(':- a .')
    assert not f('a :- b :- c.')


def test_old_ops():
    assert f('a :- b , c.')
    assert f('a :- b ; c.')
    assert f('a :- b , \t c , \t d  \n , \t c \n , b.')
    assert f('aaa :- aaa ; aaa , aaa ; aaa , aaa .')
    assert not f('a :- b ,, c.')
    assert not f('a :- , c b.')
    assert f('a :- b\t;\tc.')


def test_old_brackets():
    assert f('a :- b , (c ; d).')
    assert f('a :- (b ; c) , d.')
    assert f('a :- (((((b , c) ; d) , e) ; f) ; g) , h. ')
    assert f('a :- (a ; a) , (a ; a).')
    assert f('a :- (a).')
    assert not f('a :- (a.')
    assert f('a :- ((b ; c) , (d) ; e) , (a , b , (c ; (d))).')
    assert not f('(a :- b.)')
    assert not f('a :- () , b.')
    assert f('a :- a,(a,(a,(a,(a,(a,(a,a)))))).')


def test_old_multiple():
    assert f('a. b.')
    assert f('a:-b.\nc.\td:-e,f.')
    assert f('a.a.a.a.a.a.a.a.a.')
    assert f('a:-b.b:-a.')
    assert not f('a :- . b.')
    assert not f('...')
    assert not f('a :- a. :- a.')


def test_etc():
    assert not f('a :- b')
    assert not f('a :- . b')
    assert f('o_o.')
    assert not f('.')


def test_atoms():
    assert f('a b c :- a b c.')
    assert f('a (b c) :- a (b c).')
    assert f('a (b).')
    assert f('a (((((b))))).')
    assert f('a (b c d) (e f g).')
    assert f('a (b c) d (e (f g)).')
    assert f('f  :- a (a (a)).')
    assert f('odd (cons H (cons H1 T)) (cons H T1) :- odd T T1.')
    assert f('odd (cons H nil) nil.')
    assert f('odd nil nil.')
    assert not f('(a) :- (b).')
    assert not f('a (b ()).')
    assert f('f :- (g).')
    assert not f('a ((b) c).')
    assert not f('f :- ((b) a).')
    assert not f('a ((a b) (a b)).')
    assert f('a (a b) (a b).')


def test_complex():
    assert f('f :- g, h; t.')
    assert f('f :- g, (h; t).')
    assert f('f a :- g, h (t c d).')
    assert f('f (cons h t) :- g h, f t.')
    assert f(
        'odd (cons H (cons H1 T)) (cons H T1) :- odd T T1.\nodd (cons H nil) nil.\nodd nil nil.')
    assert f('f (g (h t)) :- ((f; g), (r), (h, t)), a; b; c.')
