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
print(contatos)
arquivo.close()