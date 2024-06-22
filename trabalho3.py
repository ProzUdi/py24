alunos = []
contador = 0
while (contador < 20):
    aluno = {}
    aluno["nome"] = input("Digite o nome:")
    aluno["prova"] = float(input("Digite a nota de prova:"))
    aluno["trabalho"] = float(input("Digite a nota de trabalho:"))
    aluno["ead"] = float(input("Digite a nota de EAD:"))
    aluno["atividade"] = float(input("Digite a nota da atividade:"))
    alunos.append(aluno)
    contador +=1

for aluno in alunos:
    soma = (aluno["prova"] + aluno["trabalho"] + aluno["ead"] + aluno["atividade"])

    print(aluno['nome']," - ",soma)
