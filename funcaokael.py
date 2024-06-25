def somar(num1, num2):
    soma = num1 + num2
    return soma

def subtrair(num1, num2):
    subtracao = num1 - num2
    return subtracao

def multiplicar(num1, num2):
    multiplicacao = num1 * num2
    return multiplicacao

def dividir(num1, num2):
    divisao = num1 / num2
    return divisao

def fatorial(num1):
    fat = 1
    while num1 > 1:
        fat = fat * num1
        num1 -= 1
    return fat

opcao = ""
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

while True:
    opcao = int(input("1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Fatorial\n6- Sair\n"))
    if opcao == 1:
        print("A soma dos numeros é : ",somar(numero1, numero2))
    if opcao == 2:
        print("A subtração dos numeros é : ",subtrair(numero1, numero2))
    if opcao == 3:
        print("A multiplicação dos números é : ", multiplicar(numero1, numero2))
    if opcao == 4:
        print("A divisão dos números é : ", dividir(numero1, numero2))
    if opcao == 5:
        print("O Fatorial do número é : ", fatorial(numero1))
    if opcao == 6:
        print("Encerrado!")
        break
        
def opcoes():
    print("1 - Mostrar listas")
    print("2 - Adicionar na listas")
    print("3 - Editar Contato")
    print("4 - Remover Contato")
    print("5 - Sair")
    opcao = int(input())
    return opcao

def lerContatos():
    arquivo = open("contatoskael.csv", "r")
    linha = arquivo.readline()

    contatos = []
    while linha != "":
        print(linha)
        contato = {}
        itens = linha.split(";")
        contato["Nome"] = itens[0]
        contato["Numero"] = itens[1].replace("\n","")
        contatos.append(contato)
        linha = arquivo.readline()
    arquivo.close()         
   
def addContato():
    contato = {}
    contato["Nome"] = input("Digite um nome: ")
    contato["Numero"] = input("Digite o numero")
    arquivo = open("contatoskael.csv" ,"a")
    arquivo.write("\n"+contato["nome"]+";"+contato["Numero"])
    arquivo.close()
    return contato

def editarContato():
    contato = {}
    contato["nome"] = input("Digite um nome: ")
    contato["numero"] = input("Digite o numero: ")
    for cont in contatos:
        if cont["nome"] == contato["nome"]:
            contato.replace("")
    return contato