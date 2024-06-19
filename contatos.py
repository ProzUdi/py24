contatos = open("contatos.csv", "r")
linha = contatos.readline()
while linha != "":
    print(linha)
    linha = contatos.readline()

contatos.close()    

#Esse é em TXT ORIGINAL<<
#contatos = open("contatos.txt", "r")
#linha = contatos.readline()
##while linha != "":
  #  print(linha)
   # linha = contatos.readline()

#contatos.close()    