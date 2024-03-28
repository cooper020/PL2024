# anasin.py
from analex import AnalisadorLexico

from ply.yacc import Yacc

class AnalisadorSintatico(Yacc):
    tokens = AnalisadorLexico.tokens

    def p_declaracao_interrogacao(self, p):
        p[0] = int(input())
        variaveis[p[1]] = p[0]

    def p_declaracao_exclamacao(self, p):
        print(p[1])

    def p_declaracao_atribuicao(self, p):
        variaveis[p[1]] = p[3]

    def p_expressao_operacao_binaria(self, p):
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3] 

    def p_expressao_agrupamento(self, p):
        p[0] = p[2]

    def p_expressao_numero(self, p):
        p[0] = p[1]

    def p_expressao_variavel(self, p):
        p[0] = variaveis.get(p[1], 0)

    def p_error(self, p):
        print("Erro de sintaxe!")

analisador_sintatico = AnalisadorSintatico()

variaveis = {}

while True:
    entrada = input('Digite uma expressão ou "sair" para encerrar: ')
    if entrada.lower() == 'sair':
        break
    if not entrada:
        continue
    analisador_sintatico.parse(entrada)
