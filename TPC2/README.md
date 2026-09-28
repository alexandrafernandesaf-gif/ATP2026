#TPC2: jogo adivinha o número
# # Autor:
Alexandra Fernandes;
114947
Foto:https://mail.google.com/mail/u/0?ui=2&ik=1b629db47d&attid=0.1&permmsgid=msg-a:r-39465701747535810&th=1a0c3fa637727b15&view=fimg&fur=ip&permmsgid=msg-a:r-39465701747535810&sz=s0-l75-ft&attbid=ANGjdJ_WTklV5L_OYpII2oSswqq-bTyrC4q0LLAlLfQ3cZ8wpF48HrC7DIEk-ODijGC2EiWUczXN7Z46Ym7hKKGKPDO23zhkbWvPke9CjdrGTAXX9dFX0x5SES3hadM&disp=emb&realattid=DA90D048-C0E3-48D0-9A52-6C5BCDFB9C1B&zw<img width="3024" height="4032" alt="image" src="https://github.com/user-attachments/assets/d5aa0b92-2330-48d9-8b50-53b1d2eece98" />



## Resumo: O trabalho de casa dado na segunda aula da teórica e prática tem como intuito criar um programa em python para o jogo "adivinha o número", em que esse mesmo jogo poderia ter duas modalidades: o computador pensa num número (entre 0 e 100)e o utilizador tenta adivinhar ou o utilizador pensa num número (entre 0 e 100) e o computador tenta adivinhar;    Quem tenta adivinhar responde com uma das afirmações: "Acertou", "O número que pensei é Maior" ou "O número que pensei é Menor". Uma vez descoberto o número o programa deve terminar imprimindo o número de tentativas que quem adivinhou usou para chegar ao resultado.

## resultados (programa em python):

# Código:
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
