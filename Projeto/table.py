#Carlos Vitor Freitas Santos - 20230014111
#Wesley Henrique da S. Vieira - 20230014390

#Biblioteca apenas para visualizar a tabela no terminal (pip install pandas)
import pandas as pd

#Requesito 1 
def criarTabela():
    print("\n-=CRIANDO TABELA=-\n")   
    tabela = {}
    nColunas = int(input("Número de colunas: "))

    for i in range (nColunas):
        nomeColuna = input(f"Nome da coluna {i}: ")
        
        linha = input(f"Digite as linhas da coluna {i} separados por (;): ").split(';')

        tabela[nomeColuna] = linha

    return tabela

#Requesito 2 
def addLinha(tabela):
    print("\n-=ADICIONANDO NOVA LINHA=-\n")  
    for key, valor in tabela.items():
        novo_item = input(f"Digite o novo item da coluna | {key}: ").capitalize()
        
        while True:
            if novo_item!="":
                break
            else:
                print("Inválido. Tente Novamente! ")
                novo_item = input(f"Digite o novo item da coluna | {key}: ")

        valor.append(novo_item)
        
    return exibir_tabela(tabela)

#Requesito 3
def delLinha(tabela):
    print("\n-=DELETANDO LINHA=-\n")  
    indice = int(input("Digite o indice que quer remover: "))
    cont_linha = list(tabela.values())

    while (indice >= len(cont_linha[0]) or indice < 0):
        print("Erro, tamanho errado!!")
        indice = int(input("Digite o indice que quer remover: "))

    for j in tabela.values():
        j.pop(indice)
    print("Removido com Sucesso!")

    return exibir_tabela(tabela)
                
#Requesito 4
def addColuna(tabela):
    print("\n-=ADICIONANDO COLUNA=-\n")  
    coluna = input("Digite o nome da nova coluna: ").capitalize()

    adicionar_coluna = input("Digite as linhas separados por (;): ").split(';')
    
    cont_linha  = list(tabela.values())

    while len(adicionar_coluna) != len(cont_linha[0]):
        print(f"Você esta adicionando mais linhas do que colunas, temos {len(cont_linha[0])}")
        adicionar_coluna = input("Digite as linhas separados por (;): ").split(';')

    tabela [coluna] = adicionar_coluna
    
    return exibir_tabela(tabela)
        

#Requesito 5
def delColuna(tabela):
    print("\n-=REMOVENDO COLUNA=-\n")
    print(f"Colunas Válidas: {[x for x in tabela.keys()]}")
    coluna_remove = input ("Digite o nome da coluna para remover: ").capitalize()
    print("\n")

    while coluna_remove not in tabela.keys():
        print ("Nome de Coluna Inválido! Tente Novamente")
        print(f"Colunas Válidas: {[x for x in tabela.keys()]}")
        coluna_remove = input ("Digite o nome da coluna para remover: ")

    tabela.pop(coluna_remove)

    return exibir_tabela(tabela)
        
#Requesito 6
def sumTable(tabela):
    print("\n-=SOMANDO OS ITENS DA TABELA=-\n")  
    soma = 0

    for i in tabela.values():
        for j in i:
            if type(j)==str:
                pass
            else:
                soma += int(j)
    if soma==0:
        return "Não possui Inteiros\n"
    else:
        return soma

#Requesito 7
def mediaTable(tabela):
    print("\n-=MÉDIA DOS ITEMS DA TABELA=-\n")  
    soma = 0
    cont = 0

    for i in tabela.values():
        for j in i:
            if type(j)==str:
                pass

            else:
                soma += int(j)
                cont += 1
    if cont == 0:
        return 'Não possui Inteiros\n'
    else:
        return (soma/cont)

#Requesito 8
def exibir_tabela(tabela):
    print("\n-=EXIBINDO A TABELA=-\n")  
    print(pd.DataFrame(tabela))

#Requesito 9
def openCSV():
    print("\n-=ABRINDO ARQUIVO .CSV=-\n")
    nova_tabela = {}
    colunas = ["Nome", "Dano Corpo", "Dano Cabeça"]

    for coluna in colunas:
        nova_tabela[coluna] = []

    with open('Projeto/valorantArmas.csv', 'r') as arqCsv:
        arqCsv.readline()

        for linha in arqCsv:
            linhas = linha.strip().split(',')
            
            for i in range(len(colunas)):
                nova_tabela[colunas[i]].append(linhas[i])

    return nova_tabela

#Requesito 10
def filtarTable(armaDano, primeiraLetra):
    print("\n-=APLICANDO FILTRO=-\n")
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
    
    
#Funções Auxiliar

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