import funcoes as fun

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

soma = fun.somar(num1, num2)
sub = fun.subtrair(num1, num2)
mult = fun.multiplicar(num1, num2)
div = fun.dividir(num1, num2)

fatorial = fun.fatorial(num1)

print(soma)
print(sub)
print(mult)
print(div)
print(fatorial)

