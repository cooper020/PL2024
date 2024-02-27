import re

def somador(caminho_arquivo):
    soma = 0
    on = False  # Começa desligado
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            for match in re.finditer(r'(on|off|=|-\d+|\d+)', linha, re.IGNORECASE):
                palavra = match.group()
                if palavra.lower() == 'on':
                    on = True
                elif palavra.lower() == 'off':
                    on = False
                elif palavra == '=':
                    print("Soma neste ponto:", soma)
                elif palavra.startswith('-'):
                    soma += int(palavra)
                elif on and palavra.isdigit():
                    soma += int(palavra)

def main():
    caminho_arquivo = input("Digite o caminho para o arquivo de texto: ")
    somador(caminho_arquivo)

if __name__ == "__main__":
    main()

