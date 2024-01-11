#Carlos Vitor Freitas Santos - 20230014111
#Wesley Henrique da S. Vieira - 20230014390

#Biblioteca para visualizar a tabela no terminal (pip install pandas)
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
            print("Removido com sucesso!")
        else:
            print("Inválido")
                
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
    print (soma)

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
    print (soma/cont)

#Requesito 8
def exibir_tabela(tabela):
    print(tabela)

#Requesito 9
def openCSV():
    return None   

#Requesito 10
def filtarTable():
    return None



