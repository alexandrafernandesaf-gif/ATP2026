#TPC3: jogo corrida para os 100
# # Autor:
Alexandra Fernandes;
114947
Foto:<img width="3024" height="4032" alt="image" src="https://github.com/user-attachments/assets/d5aa0b92-2330-48d9-8b50-53b1d2eece98" />



## Resumo: O trabalho de casa (TPC3) tem como intuito criar um programa em Python para o jogo "Corrida para os 100", em que o total começa em 0 e dois jogadores (o utilizador e o computador) alternam somando um número de 1 a 10 ao total acumulado, vencendo quem atingir exatamente o número 100. O jogo conta com duas modalidades: o computador joga em primeiro lugar (devendo utilizar a estratégia vencedora para ganhar sempre) ou o utilizador joga em primeiro lugar (podendo o computador ganhar ou perder consoante as jogadas do utilizador). A cada jogada, o programa deve validar o valor introduzido, somar a jogada do computador, apresentar o total da ronda e terminar no momento exato em que um dos jogadores atinge o número 100, declarando o respetivo vencedor.

## resultados (programa em python):

# Código:
total=1 # assim o numero 1 que o pc joga logo no inicio fica ja adicionado
jogada_computador=0
def onze_menos(numero):
    return 11-numero
start=str(input("Quem queres que comece a jogar, tu ou o computador?"))
if start=="computador":
    jogada_computador=1
    print(f"computador joga {jogada_computador}")
    while total<100:
        numero=int(input("É a tua vez de jogar, escreve um número de 1 a 10"))
        jogada_computador=onze_menos(numero)
        print(f"computador joga {jogada_computador}")
        total=numero+onze_menos(numero)+total
        print(f"O total da ronda foi {total}")
    print("O computador venceu o jogo!")
elif start=="eu":
    total=0
    while total<100:
        numero1=int(input("É a tua vez de jogar, escreve um número de 1 a 10"))
        total=total+numero1
        if total==100:
            print("Venceste o jogo, chegaste aos 100!")
            break
        jogada_computador=onze_menos(numero1)
        print(f"computador joga {jogada_computador}")
        total=total+numero1+jogada_computador
        if total==100:
            print("O computador venceu o jogo pois chegou aos 100!")
            break
        print(f"O total da ronda foi {total}")
