import re

produtos = [
    {"nome": "Água Fastio", "preco": 60, "id": 1},
    {"nome": "Coca-Cola", "preco": 90, "id": 2},
    {"nome": "Bolo Chocolate", "preco": 75, "id": 3},
    {"nome": "Panike Chocolate", "preco": 80, "id": 4},
    {"nome": "Folhado Misto", "preco": 85, "id": 5},
    {"nome": "Compal Manga-Laranja", "preco": 90, "id": 6},
    {"nome": "Frisumo", "preco": 90, "id": 7},
    {"nome": "Capri-sun", "preco": 90, "id": 8},
    {"nome": "Croissant Misto", "preco": 80, "id": 9},
    {"nome": "Bolo Cenoura", "preco": 75, "id": 10},
    {"nome": "Mars", "preco": 80, "id": 11},
    {"nome": "M&Ms", "preco": 80, "id": 12},
    {"nome": "Pão Chouriço", "preco": 110, "id": 13},
]

tokens = [
    ('LISTAR',  r'^LISTAR$'),
    ('SAIR',  r'^SAIR$'),
    ('SELECIONAR',  r'^SELECIONAR\s(\d+)$'),
    ('MOEDA', r'^MOEDA\s((1e,?|2e,?|1c,?|2c,?|5c,?|10c,?|20c,?|50c,?)+)$')
]

def analisador_lexico(texto):
    for tipo, regex in tokens:
        match = re.match(regex, texto)
        if match:
            return tipo, match.groups()
    print("[NOT FOUND] Input aceitável")
    return None, None 

        
def analisador_gramatical(tipo, args):
    if tipo == "LISTAR":
        return "listar"
    elif tipo == "MOEDA":
        moedas = re.findall(r'\d+e|\d+c', args[0])
        return "moeda", [int(valor[:-1])*100 if valor[-1]=='e' else int(valor[:-1]) for valor in moedas]
    elif tipo == "SELECIONAR":
        return "selecionar", int(args[0])
    elif tipo == "SAIR":
        return "sair"
    raise ValueError(f"Comando inválido: {tipo} {args}")
    

def saldo(moedas):
    return sum(moedas)  

def display_saldo(saldo):
    euros = saldo // 100 
    cents = saldo % 100  
    return f"{euros}e{cents}c"

    
def comprar(produto, saldo):
    if saldo >= produto["preco"]:
        return saldo - produto["preco"], produto 
    else:
        raise ValueError(f"[SALDO] Não tens suficiente: {saldo} < {produto['preco']}")
               

def listar(produtos):
    for produto in produtos:
        print(f"{produto['id']} => {produto['nome']} | {display_saldo(produto['preco'])}\n")


def main():
    moedas = []
    while True:
        inp = input(">> ").strip()
        tipo, args = analisador_lexico(inp)
        if tipo is None:
            continue
        com = analisador_gramatical(tipo, args)

        if com == "listar":
            listar(produtos)

        elif com[0] == "moeda":
            moedas += com[1] 
            print(f"Saldo: {display_saldo(saldo(moedas))}")

        elif com[0] == "selecionar":
            produto = produtos[com[1] - 1]
            try:
                troco, produto = comprar(produto, saldo(moedas))
                print(f"Produto: {produto['nome']}")
                print(f"Saldo: {troco}c") 
                moedas = [troco] 
            except ValueError as e:
                print(str(e))

        elif com == "sair":
            print(f"Troco: {display_saldo(saldo(moedas))}") 
            print("ADEUS e OBRIGADO!")
            break




if __name__ == "__main__":
    main()
