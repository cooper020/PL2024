import sys

def process_data():
    lista_mod = []
    lista_int1 = [] 
    lista_int2 = [] 
    lista_int3 = [] 
    lista_int4 = [] 
    lista_int5 = [] 
    primeira_linha = True
    numero_total = 0
    aptos = 0
    inaptos = 0

    for linha in sys.stdin:
        if primeira_linha:
            primeira_linha = False
            continue

        emd = linha.strip().split(',')

        if emd[8].lower() not in lista_mod:
            lista_mod.append(emd[8].lower())

        numero_total += 1

        if emd[12] == 'true':
            aptos += 1
        else:
            inaptos += 1  

        if 19 < int(emd[5]) < 25:
           lista_int1.append(emd[2])
        elif 24 < int(emd[5]) < 30:
           lista_int2.append(emd[2]) 
        elif 29 < int(emd[5]) < 35:
           lista_int3.append(emd[2]) 
        elif 34 < int(emd[5]) < 40:
           lista_int4.append(emd[2]) 
        else:
           lista_int5.append(emd[2])                              

    lista_mod.sort()

    return lista_mod, numero_total, aptos, inaptos, lista_int1, lista_int2, lista_int3, lista_int4, lista_int5

def print_results(lista_mod, numero_total, aptos, inaptos, lista_int1, lista_int2, lista_int3, lista_int4, lista_int5):
    if numero_total > 0:
        percentagem_apt = round((aptos*100) / numero_total, 2)
        percentagem_inapt = round((inaptos*100) / numero_total, 2)
    else:
        percentagem_apt = percentagem_inapt = 0

    if numero_total > 0:
        p_20_24 = round((len(lista_int1)*100) / numero_total, 2)
        p_25_29 = round((len(lista_int2)*100) / numero_total, 2)
        p_30_34 = round((len(lista_int3)*100) / numero_total, 2)
        p_35_39 = round((len(lista_int4)*100) / numero_total, 2)
        p_19_40 = round((len(lista_int5)*100) / numero_total, 2)

    print("1. lista_mod ordenada alfabeticamente das modalidades desportivas:\n",lista_mod)
    print()
    print("2. Percentagens de atletas aptos e inaptos para a prática desportiva: ")
    print("Percentagem de atletas aptos:", percentagem_apt, "%")
    print("Percentagem de atletas inaptos:", percentagem_inapt, "%")
    print()
    print("3. Distribuição de atletas por escalão etário:")
    print("Faixa etária [20-24]: Número de atletas", len(lista_int1), "| Percentagem:", p_20_24, "%")
    print("Faixa etária [25-29]: Número de atletas", len(lista_int2), "| Percentagem:", p_25_29, "%")
    print("Faixa etária [30-34]: Número de atletas", len(lista_int3), "| Percentagem:", p_30_34, "%")
    print("Faixa etária [35-39]: Número de atletas", len(lista_int4), "| Percentagem:", p_35_39, "%")
    print("Faixas etária [<19 e >40]: Número de atletas", len(lista_int5), "| Percentagem:", p_19_40, "%")
    

lista_mod, numero_total, aptos, inaptos, lista_int1, lista_int2, lista_int3, lista_int4, lista_int5= process_data()
print_results(lista_mod, numero_total, aptos, inaptos, lista_int1, lista_int2, lista_int3, lista_int4, lista_int5)



