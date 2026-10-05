# Implementação do jogo
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
    