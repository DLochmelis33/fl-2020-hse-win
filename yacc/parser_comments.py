#! /usr/bin/env python3

import ply.yacc as yacc_c
from lexer_comments import tokens, lexer
import sys

uncommented = ""


def p_omit_comments(p):
    '''uncommented  : ANYOTHER
                    | ANYOTHER COMSTART uncommented COMEND uncommented '''
    if len(p) == 2:
        p[0] = p[1]  # string
    else:
        p[0] = p[1] + p[5]  # strings
    global uncommented
    uncommented = str(p[0])


def p_error(p):
    if p:
        raise SyntaxError('yay \'' + p.value +
                          '\' at line ' + str(p.lexer.lineno))
    raise SyntaxError('Expected yay, but got none')


parser = yacc_c.yacc()


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        with open(arg, 'r') as inFile:
            parser.parse(inFile.read())
            with open(arg + '.ou', 'w') as outFile:
                # with sys.stdout as outFile:
                print(uncommented, file=outFile)
