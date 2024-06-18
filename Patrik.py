import funcoes as func

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: " ))

somar = func.somar(numero1, numero2)
subtrair = func.subtrair(numero1, numero2)
multiplicacao = func.multiplicacao(numero1, numero2)
divisao = func.divisao(numero1, numero2)
fatorial = func.fatorial(numero1)

print(somar)
print(subtrair)
print(multiplicacao)
print(divisao)
print(fatorial)