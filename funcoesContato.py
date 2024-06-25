def opcoes():
    print("1 - Mostrar listas")
    print("2 - Adicionar na listas")
    print("3 - Editar Contato")
    print("4 - Sair")
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
    contatos = []
    contato = {}
    contato["nome"] = input("Digite um nome: ")
    contato["numero"] = input("Digite o numero: ")
    cont["nome"] = input("Digite um nome que deseja editar: ")
    cont["numero"] = input("Digite o novo numero")
    for cont in contatos:
        if cont["numero"] == contato["numero"]:
            contato.replace(contato["nome"],cont["nome"])
    return contato