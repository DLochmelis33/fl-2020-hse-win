import ply.lex as lex

tokens = [
    'ID',
    'CORKSCREW',  # :)
    'DISJ',
    'CONJ',
    'LPAREN',
    'RPAREN',
    'DOT'
]


t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_CORKSCREW = r':-'
t_DISJ = r';'
t_CONJ = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    if t:
        raise SyntaxError("Illegal character '" +
                          str(t.value[0]) + "' at line " + str(t.lexer.lineno))
    raise SyntaxError('Expected character but got none')


lexer = lex.lex()
