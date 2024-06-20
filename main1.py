import funcoes1 as funcoes

contatos = funcoes.lerContatos()

opcao = 0
while opcao != 3:
  opcao = funcoes.opcoes()
  if(opcao == 1):
    print("Nome - Telefone")
    for contato in contatos:
      print(f"{contato}")
  elif(opcao == 2):
    contatos.append(funcoes.addContato())
  elif(opcao == 3):
    print("Obrigado por usar o sistema")
  else:
    print("Opção invalida")