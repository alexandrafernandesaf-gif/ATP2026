y=int(input("qual jogo desejas jogar o 1 ou o 2?"))
if y==1:
    limite_inferior=0
    limite_superior=100
    hipotese=(limite_inferior+limite_superior)//2
    tentativas=0
    x="início "
    while x != "acertou":
        x=str(input(f"o número que pensaste é o {hipotese}?"))
        if x== "o número que pensei é maior":
            limite_inferior=hipotese+1
            hipotese=(limite_inferior+limite_superior)//2
            tentativas=tentativas+1
        elif x== "o número que pensei é menor":
            limite_superior=hipotese-1
            hipotese=(limite_superior+limite_inferior)//2
            tentativas=tentativas+1
    print(f"acertou o número em {tentativas} tentativas")

elif y==2:
    import random
    numero=random.randint(0, 100)
    tentativas = 0
    z="início"
    while numero != z:
        z=int(input("Pensei num número entre 0 e 100. Tente adivinhar, podes começar?"))
        hipotese= int(input("Qual é a tua hipótese? "))
        if hipotese>numero:
            print("O número que pensei é Menor!")
            tentativas=tentativas+1
        elif hipotese < numero:
            print("O número que pensei é Maior!")
            tentativas=tentativas+1
        else:
            print(f"acertaste o número que pensei em {tentativas} tentativas")
else:
    print("não existe mais jogos para além do 1 e do 2")
    
   
