import funcoes

num1 = int(input("Digite um  numero:"))
num2 = int(input("Digite outro numero:"))
soma = funcoes.somar(num1, num2)

subtracao = funcoes.subtrair(num1, num2)

multiplicar = funcoes.multiplicar(num1, num2)

dividir = funcoes.dividir(num1, num2)

fat1 = funcoes.fatorial(num1)
fat2 = funcoes.fatorial(num2)

print(fat1)
print(fat2)
print(soma)
print(subtracao)
print(multiplicar)
print(dividir)
