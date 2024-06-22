votos = {}
voto = 0
while(voto != -1):
    voto = int(input("Digite o numero do seu candidato: "))
    if voto in votos:
        votos[voto] += 1
    else:
        votos[voto] = 1
    print("Voto registrado")
print(votos)
