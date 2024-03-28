# analex.py
from ply.lex import Lex

class AnalisadorLexico(Lex):
    tokens = (
        'VARIAVEL',
        'NUMERO',
        'SOMA',
        'SUBTRACAO',
        'MULTIPLICACAO',
        'DIVISAO',
        'ABRE_PARENTESES',
        'FECHA_PARENTESES',
        'ATRIBUICAO',
        'INTERROGACAO',
        'EXCLAMACAO',
    )

    t_SOMA = r'\+'
    t_SUBTRACAO = r'-'
    t_MULTIPLICACAO = r'\*'
    t_DIVISAO = r'/'
    t_ABRE_PARENTESES = r'\('
    t_FECHA_PARENTESES = r'\)'
    t_ATRIBUICAO = r'='
    t_INTERROGACAO = r'\?'
    t_EXCLAMACAO = r'!'

    def t_VARIAVEL(self, t):
        r'[a-zA-Z][\w]*'
        return t

    def t_NUMERO(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_ignore(self, t):
        r' \t'

    def t_error(self, t):
        print(f"Caractere inválido '{t.value[0]}'")
        t.lexer.skip(1)

analisador_lexico = AnalisadorLexico()
