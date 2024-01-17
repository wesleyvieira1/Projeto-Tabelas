#Carlos Vitor Freitas Santos - 20230014111
#Wesley Henrique da S. Vieira - 20230014390

#Biblioteca apenas para visualizar a tabela no terminal (pip install pandas)
import pandas as pd

#Requesito 1 
def criarTabela():    
    tabela = {}
    nColunas = int(input("Número de colunas: "))

    for i in range (nColunas):
        nomeColuna = input("Nome da coluna: ")
        linha = input("Digite as linhas separados por (;): ").split(';')

        tabela[nomeColuna] = linha

    return tabela

#Requesito 2 
def addLinha(tabela):
    for key, valor in tabela.items():
        novo_item = input(f"Digite o novo item da coluna | {key}: ")
        
        while True:
            if novo_item!="":
                break
            else:
                print("Inválido. Tente Novamente! ")
                novo_item = input(f"Digite o novo item da coluna | {key}: ")

        valor.append(novo_item)

#Requesito 3
def delLinha(tabela):
    indice = int(input("Digite o indice que quer remover: "))

    for i in tabela.values():
        if indice<len(i):
            i.pop(indice)
            return("Removido com sucesso!")
        
        else:
            return("Inválido")
                
#Requesito 4
def addColuna(tabela):
    coluna = input("Digite o nome da nova coluna: ")
    adicionar_coluna = input("Digite as linhas separados por (;): ").split(';')
    
    tabela [coluna] = adicionar_coluna
        

#Requesito 5
def delColuna(tabela):
    coluna_remove = input ("Digite o nome da coluna para remover: ")

    while coluna_remove not in tabela.keys():
        print ("Invalido")
        coluna_remove = input ("Digite o nome da coluna para remover: ")

    tabela.pop(coluna_remove)
    
#Requesito 6
def sumTable(tabela):
    soma = 0

    for i in tabela.values():
        for j in i:
            if type(j)==str:
                pass

            else:
                soma += int(j)

    return soma

#Requesito 7
def mediaTable(tabela):
    soma = 0
    cont = 0

    for i in tabela.values():
        for j in i:
            if type(j)==str:
                pass

            else:
                soma += int(j)
                cont += 1

    return soma/cont

#Requesito 8
def exibir_tabela(tabela):
    print(pd.DataFrame(tabela))

#Requesito 9
def openCSV():
    nova_tabela = {}
    colunas = ["Nome", "Dano Corpo", "Dano Cabeça"]

    for coluna in colunas:
        nova_tabela[coluna] = []

    with open('valorantArmas.csv', 'r') as arqCsv:
        arqCsv.readline()

        for linha in arqCsv:
            linhas = linha.strip().split(',')
            
            for i in range(len(colunas)):
                nova_tabela[colunas[i]].append(linhas[i])

    return pd.DataFrame(nova_tabela)

#Requesito 10

#Filtro 1
def armaDano():
    valor = int(input("Digite qual dano na cabeça você quer filtrar: "))
    tab = openCSV()
    cont = 0
    for i in tab["Dano Cabeça"]:
        if int(i) > valor:
            nome = tab["Nome"][cont]
            print(f"{nome}: {i}")
        cont += 1

#Filtro 2
def primeiraLetra():
    letra = str(input("Digite uma letra que vc quer filtrar: ")).upper()
    while True:
        if len(letra)>1:
            print("DIGITE APENAS UMA LETRA. Tente Novamente! ")
            letra = str(input("Digite uma letra que vc quer filtrar: ")).upper()
        else:
            tab = openCSV()
            for i in tab["Nome"]:
                if letra in i:
                    print(i)
            break

def filtarTable(armaDano, primeiraLetra):
    print('''O que você quer filtrar:
          
            [1] - Dano na Cabeça
            [2] - Primeira Letra
          ''')
    
    opc = int(input("Digite a opc: "))
    print("\n")
    
    if opc==1:
        return armaDano()
    else:
        return primeiraLetra()

