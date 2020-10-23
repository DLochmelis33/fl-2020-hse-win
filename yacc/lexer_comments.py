import ply.lex as lex_c

tokens = [
    'COMMENT',
    'ANYOTHER'
]

t_ignore = ' \t'
t_COMMENT = r'\(\*(.\n*)+?\*\)'
t_ANYOTHER = r'((?!\(\*).)+'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    if t:
        raise SyntaxError("Illegal character '" +
                          str(t.value[0]) + "' at line " + str(t.lexer.lineno))
    raise SyntaxError('Expected character but got none')


lexer = lex_c.lex()
