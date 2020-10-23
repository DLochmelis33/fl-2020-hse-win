#! /usr/bin/env python3

import ply.yacc as yacc
from lexer import tokens, lexer
import sys

program = ('NONE', [])


def p_program(p):
    '''program : decl_seq'''
    global program
    program = ('PROGRAM', p[1])


def p_decl_seq(p):  # list!
    '''decl_seq	: decl
                | decl decl_seq'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]


def p_decl(p):
    '''decl : head CORKSCREW body DOT
            | head DOT'''
    if len(p) == 3:
        p[0] = ('DECL', [p[1]])
    else:
        p[0] = ('DECL', [p[1], p[3]])


def p_head(p):
    'head : atom'
    p[0] = ('HEAD', [p[1]])


def p_atom(p):
    '''atom : ID
            | ID atom_seq'''
    if len(p) == 2:
        p[0] = ('ATOM \'' + p[1] + '\'', [])
    else:
        p[0] = ('ATOM \'' + p[1] + '\'', p[2])


def p_atom_paren(p):  # type equal to atom
    '''atom_paren   : LPAREN atom_paren RPAREN
                    | LPAREN atom RPAREN'''
    p[0] = p[2]


def p_atom_simple(p):
    '''atom_simple : ID'''
    p[0] = ('ATOM \'' + p[1] + '\'', [])


def p_atom_seq(p):  # list!
    '''atom_seq : atom_simple
                | atom_paren
                | atom_simple atom_seq
                | atom_paren atom_seq'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]


def p_body(p):
    'body : expr_disj'
    p[0] = ('BODY', [p[1]])


def p_expr_disj(p):
    '''expr_disj 	: expr_conj DISJ expr_disj
                    | expr_conj'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('DISJ', [p[1], p[3]])


def p_expr_conj(p):
    '''expr_conj 	: expr_paren CONJ expr_conj
                    | expr_paren'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('CONJ', [p[1], p[3]])


def p_expr_paren(p):
    '''expr_paren 	: atom
                    | LPAREN expr_disj RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_error(p):
    if p:
        raise SyntaxError('Couldn\'t parse token \'' + p.value +
                          '\' at line ' + str(p.lexer.lineno))
    raise SyntaxError('Expected token, but got none')


# def print_ast(p, indent=0, file=sys.stdout):
#     (node, children) = p
#     for i in range(0, indent):
#         print('- ', end='', file=file)
#     print(node, end='\n', file=file)
#     for c in children:
#         print_ast(c, indent + 1, file)


def print_ast_ultra(p, indentList=[], file=sys.stdout):
    (node, children) = p
    if len(indentList) > 1:
        for t in range(len(indentList)-1):
            print('|  ', end='', file=file) if indentList[t] else print(
                '   ', end='', file=file)
    if len(indentList) > 0 and not indentList[-1]:
        print(' `-', end='', file=file)
    elif len(indentList) > 0:  # decl level
        print('|`-', end='', file=file)
    print('' + node, end='\n', file=file)
    if len(children) > 1:
        for i in range(len(children) - 1):
            print_ast_ultra(children[i], indentList + [1], file)
    if len(children) > 0:
        print_ast_ultra(children[-1], indentList + [0], file)


parser = yacc.yacc()

if __name__ == "__main__":
    # if len(sys.argv) == 1:
    #     sys.argv += ['in.txt']
    for arg in sys.argv[1:]:
        with open(arg, 'r') as inFile:
            parser.parse(inFile.read())
            with open(arg + 't', 'w') as outFile:
                # with sys.stdout as outFile:
                print_ast_ultra(program, [], outFile)
