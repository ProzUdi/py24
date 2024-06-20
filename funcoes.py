def somar(num1, num2):
  return num1 + num2

def subtrair(num1, num2):
  return num1 - num2

def multiplicar(num1, num2):
  return num1 * num2

def dividir(num1, num2):
  if (num2 == 0):
    print("Não pode fazer divisão por zero")
    return 0
  
  return num1 / num2

def fatorial(num):
  if (num == 1):
    return 1
  
  return num * fatorial(num -1)

def opcoes():
  print("1 - Ler contatos")
  print("2 - Adicionar Contato")
  print("3 - Sair")
  opcao = int(input())
  return opcao

def lerContatos():
  arquivo = open("contatos.csv", "r")
  linha = arquivo.readline()

  contatos = []
  while linha != "":
    contato = {}
    items = linha.split(";")
    contato["nome"] = items[0]
    contato["telefone"] = items[1].replace("\n","")
    contatos.append(contato)
    linha = arquivo.readline()
  arquivo.close()
  return contatos

def addContato():
  contato = {}
  contato["nome"] = input("Digite o nome: ")
  contato["telefone"] = input("Digite o telefone: ")
  arquivo = open("contatos.csv", "a")
  arquivo.write(contato["nome"]+";"+contato["telefone"])
  arquivo.close()
  return contato

