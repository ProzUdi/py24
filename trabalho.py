emails = []
def opcoes():
  print("1 - incluir e-mails")
  print("2 - remover e-mails")
  print("3 - editar e-mails")
  print("4 - sair")
  opcao = int(input())
  return opcao

opcao = 0
while opcao != 4:
  opcao =opcoes()
  if(opcao == 1):
    emails.append(input("Digite os e-mails que deseja inclur: "))
  elif(opcao == 2):
    emails.remove(input("Escreva os e-mails que deseja excluir: "))
  elif(opcao == 3):
    emails.remove(input("Digite o e-mail que deseja editar: "))
    emails.append(input("Digite o e-mail editado: "))
  elif(opcao == 4):
    break
print(emails)
