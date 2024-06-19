contatos = open("contatos.txt", "r")
linha = contatos.readline()
while linha != "":
    print(linha)
    linha = contatos.readline()

contatos.close()    