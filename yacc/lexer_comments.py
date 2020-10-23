import ply.lex as lex_c

tokens = [
    # 'COMMENT',
    'ANYOTHER',
    'COMSTART',
    'COMEND'
]

t_ignore = ' \t'
# t_COMMENT = r'\(\*(.\n*)+?\*\)'
t_ANYOTHER = r'((?!(\(\*)|(\*\))).\s*\n*)+'
t_COMSTART = r'\(\*'
t_COMEND = r'\*\)'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    if t:
        raise SyntaxError("Illegal yaracter '" +
                          str(t.value[0]) + "' at line " + str(t.lexer.lineno))
    raise SyntaxError('Expected yaracter but got none')


lexer = lex_c.lex()
