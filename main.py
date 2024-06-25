import funcoesContato as funcoes
contatos = funcoes.lerContatos()
opcao = 0
while opcao != 5:
  opcao = funcoes.opcoes()
  if(opcao == 1):
    print("Nome - Telefone")
    for contato in contatos:
      print(f"{contato}")
  elif(opcao == 2):
    contatos.append(funcoes.addContato())
  elif(opcao == 3):
    funcoes.editarContato(contatos)
  elif(opcao == 4):
    funcoes.excluirContato(contatos)
  elif(opcao == 5):
    print("Obrigado por usar o sistema")
  else:
    print("Opção invalida")
