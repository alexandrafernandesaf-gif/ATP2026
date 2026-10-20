#TPC5: Aplicação gestão de alunos
# # Autor:
Alexandra Fernandes;
114947
Foto:<img width="3024" height="4032" alt="image" src="https://github.com/user-attachments/assets/d5aa0b92-2330-48d9-8b50-53b1d2eece98" />



## Resumo: O TPC5 tem como intuito criar uma aplicação em Python para a gestão de alunos, considerando um modelo em que o aluno é representado por dados que incluem o nome, o ID e uma lista com três notas (nota de TPC, de projeto e de teste), e a turma é constituída por uma lista desses alunos. Esta aplicação deve colocar no monitor um menu interativo de operações que permite criar uma turma, inserir um aluno, listar a turma, consultar um aluno por ID, guardar ou carregar a turma de um ficheiro, e sair da aplicação. No fim da execução de cada operação selecionada, a aplicação deve apresentar novamente o menu e pedir ao utilizador a opção para continuar, repetindo-se até o programa ser terminado, sendo o objetivo final utilizar esta aplicação desenvolvida para criar uma turma com 5 alunos.

## resultados (programa em python):

# Código:
def menu():
    print(""" 
    (1) Criar uma turma
    (2) Inserir um aluno na turma
    (3) Listar a turma
    (4) Consultar um aluno por id
    (8) Guardar a turma em ficheiro
    (9) Carregar uma turma dum ficheiro
    (0) Sair da aplicação 
    """)
#funçao para criar uma turma
def criar_turma():
    turma=[]
    return turma

#inserir aluno na turma
def inserir_aluno(turma,aluno):
    turma.append(aluno)
    return turma

#listar a turma
def listar_turma(turma):
    return turma

#consultar aluno por id
def consultar_id(turma,id):
    for aluno in turma:
        if aluno[1]==id:
            return aluno 

#guardar a turma num ficheiro
def guardar_turma(turma, fnome):
    file = open(fnome,"w") # "r", "w" pode ler e editar read e write
    for aluno in turma:
        file.write(str(aluno) + "\n")
    file.close()
    
#carregar turma de ficheiros
def recuperar_turma(fnome):
    file = open(fnome, "r")  # "r" serve para ler o ficheiro
    turma = file.read()      # lê todo o conteúdo do ficheiro
    file.close()             # fecha o ficheiro
    return turma

numero=""
turma=[]
while numero != 0:
    menu()
    numero=int(input("Introduza a opção que deseja realizar"))
    if numero==1:
        letra=str(input("Introduz a letra que será atribuída à turma que está a criar"))
        criar_turma()
        print(f"A turma {letra} foi criada com sucesso ")
        
    elif numero==2:
        nome = str(input("Nome do aluno: "))
        id_aluno = int(input("ID do aluno: "))
        tpc = float(input("Nota TPC: "))
        proj = float(input("Nota Projeto: "))
        teste = float(input("Nota Teste: "))
        aluno = (nome, id_aluno, [tpc, proj, teste])
        inserir_aluno(turma, aluno)
        print("Aluno inserido com sucesso!")
    
    elif numero==3:
        print(f"A lista da turma é {listar_turma(turma)}")
    
    elif numero==4:
        id=int(input("Introduza o ID do aluno que pretende encontrar"))
        for aluno in turma:
            if aluno[1]== id:
                consultar_id(turma, id)
                print(f"O aluno que procura é {consultar_id(turma, id)}")
    
    elif numero==8:
        fnome=str(input("Introduza o nome que pretende atribuir ao ficheiro que será guardado"))
        guardar_turma(turma, fnome)
        print("A sua turma foi guardada com sucesso ") 
    elif numero==9:
        fnome=str(input("Introduza a turma que procura"))
        recuperar_turma(fnome)
        print("A turma foi recuperada com sucesso")
    elif numero==0:
        print("A sair da aplicação")
    else:
        print("Não existe essa opção na aplicação, tente novamente")


