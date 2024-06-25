def opcoes():
  print("1 - Ler contatos")
  print("2 - Adicionar Contato")
  print("3 - Editar Contato")
  print("4 - Excluir Contato")
  print("5 - Sair")
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
  arquivo.write("\n"+contato["nome"]+";"+contato["telefone"])
  arquivo.close()
  return contato

def editarContato(contatos):
  contatoEdicao = {}
  contatoEdicao["nome"] = input("Digite o nome que deseja editar: ")
  contador = 0
  encontrado = False
  for contato in contatos:
    if (contatoEdicao["nome"] == contato["nome"]):
      encontrado = True
      print("O numero atual é: ",contato["telefone"])
      contatoEdicao["telefone"] = input("Digite o novo numero do telefone: ")
      contatos[contador] = contatoEdicao
    contador +=1

  if (encontrado):
    arquivo = open("contatos.csv", "w")
    for contato in contatos:
      arquivo.write(contato["nome"]+";"+contato["telefone"]+"\n")

    arquivo.close()
  else:
    print("Contato não encontrado")

  return contatos

def excluirContato(contatos):
  contatoEdicao = {}
  contatoEdicao["nome"] = input("Digite o nome que deseja excluir: ")
  contador = 0
  encontrado = False
  for contato in contatos:
    if (contatoEdicao["nome"] == contato["nome"]):
      encontrado = True
      print("Realmente deseja excluir o numero (s/n): ",contato["telefone"])
      resposta = input()
      if (resposta == "s"):
        contatos.pop(contador)
    contador +=1

  if (encontrado):
    arquivo = open("contatos.csv", "w")
    for contato in contatos:
      arquivo.write(contato["nome"]+";"+contato["telefone"]+"\n")

    arquivo.close()
  else:
    print("Contato não encontrado")

  return contatos


