#TPC3: jogo corrida para os 100
# # Autor:
Alexandra Fernandes;
114947
Foto:<img width="3024" height="4032" alt="image" src="https://github.com/user-attachments/assets/d5aa0b92-2330-48d9-8b50-53b1d2eece98" />

## Resumo: Este programa consiste numa aplicação interativa desenvolvida em Python para a criação, análise e manipulação de uma lista interna de números inteiros através de um menu de opções em ciclo. O sistema permite ao utilizador inicializar a lista gerando valores inteiros aleatórios entre 1 e 100 ou inserindo manualmente os elementos desejados, substituindo a lista anterior sempre que uma destas opções é selecionada. A partir da lista guardada, a aplicação disponibiliza ferramentas para calcular a soma e a média dos seus elementos, determinar o maior e o menor valor presente, verificar se a sequência se encontra ordenada de forma crescente ou decrescente, e pesquisar a posição de um determinado número, devolvendo a respetiva posição ou o valor -1 caso o elemento não seja encontrado. O programa executa continuamente as operações solicitadas, reexibindo o menu após cada ação até que o utilizador escolha a opção de sair, momento em que a aplicação termina a sua execução mostrando a lista final mantida em memória.

## resultados (programa em python):
# Código:
#tpc4 
import random
def menu():
    print(""" 
    (1) Criar Lista
    (2) Ler Lista
    (3) Soma
    (4) Média
    (5) Maior
    (6) Menor
    (7) EstaOrdenada por ordem Crescente
    (8) EstaOrdenada por ordem Decrescente
    (9) Procura um elemento
    (0) Sair
    """)

#listaaleatoria
def criarLista():
    lista=[]
    lista = random.sample(range(1, 101), 10)
    return lista
#funçaolerlista
def lerLista2():
    lista = []
    i=0
    n = int(input("Quantos números queres introduzir? "))
    while n>i:
        num = int(input("Introduz o número"))
        lista.append(num)
        i=i+1
    return lista
#funçaosoma
def soma(lista):
    soma=0
    for i in lista:
        soma = soma + i
    return soma
#funçaomedia
def media(lista):
    media=0
    soma=0
    for i in lista:
        soma = soma + i
        media = soma / len(lista) 
    return media
#funçaomaior
def maior(lista):
    maior=lista[0]
    for i in lista:
        if i>maior:
            maior=i
    return maior
#funçaomenor
def menor(lista):
    menor=lista[0]
    for i in lista:
        if i<menor:
            menor=i
    return menor
                
#funçao_ordenada_crescente
def estaOrdenadaD(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            return False
    return True

#funçao_ordenada_decrescente
def estaOrdenadaCD(lista):
    for i in range(len(lista) - 1):
        if lista[i] < lista[i+1]:
            return False
    return True


#funçao_encontrar_elem
def posição(lista,elem):
            encontrei= False #flag guarda um boleano que me permite controlar o ciclo
            i=0
            res= -1
            while i<len(lista):
                if lista[i] == elem: #nunca usar return dentro dos ciclos
                    res=i
                    i=i+1
            return res

opçao=""
lista=[]
while opçao != "0":
    menu()
    opçao=str(input("Introduz o número da opção que queres selecionar"))
    if opçao == "1":
        lista=criarLista()
        print(f"Lista aleatória criada com sucesso!{(lista)}")
        
    elif opçao == "2":
        lista=lerLista2()
        print(f"Lista criada {lista}")

    elif opçao == "3":
        if len(lista)>0:
            soma(lista)
            print(f"A soma é {soma(lista)}")
            
    elif opçao == "4":
        if len(lista)>0:
            print(f"A média é {media(lista)}")

    elif opçao == "5":
        if len(lista) > 0:
            print(f"O maior. numero da lista é {maior(lista)}")
            
    elif opçao == "6":
        if len(lista) > 0:
            print(f"O menor número da lista é {menor(lista)}")

    elif opçao == "7":
        if len(lista) > 0:
            if estaOrdenadaD(lista)==True:
                print("A tua lista está ordenada por ordem crescente")
            else:
                print("A tua lista não está ordenada")
        
    elif opçao == "8":
        ordem=0
        if len(lista) > 0:
            if estaOrdenadaCD(lista)== True:
                print("A tua lista está ordenada por ordem decrescente")
            else:
                print("A tua lista não está ordenada")
            
    elif opçao == "9":
        if len(lista) > 0:
            elem=int(input("Qual elemento pretendes encontrar?"))
            pos=posição(lista,elem)
            print(f"O elemento que procuras está na posição {pos} da tua lista")
        
    elif opçao == "0":
        print(f"A tua lista final é {lista}")
    else:
        print("Não existe essa opção no menu da nossa aplicação!")
