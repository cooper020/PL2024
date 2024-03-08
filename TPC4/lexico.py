import re

def lexer():
    texto = input("Digite o texto que pretente analisar: ")
    token_specification = [
        ('SELECT',  r'select'),               
        ('FROM',    r'from'),                 
        ('WHERE',   r'where'),                
        ('ID',      r'[a-zA-Z_]\w*'),         
        ('NUM',     r'\d+'),                  
        ('COMMA',   r','),                    
        ('GREATER_EQ', r'>='),                
        ('WHITESPACE', r'\s+'),              
        ('ERROR',   r'.'),                    
    ]
    
    pattern = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    tokens = []
    for m in re.finditer(pattern, texto):
        kind = m.lastgroup
        value = m.group()
        tokens.append((kind, value))
    return tokens


tokens = lexer()
for token in tokens:
    print(token)

