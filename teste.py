import funcoes as fun

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um outro número: "))

som = fun.somar(num1,num2)
sub = fun.subtrair(num1,num2)
mul = fun.multiplicar(num1,num2)
div = fun.dividir(num1,num2)
fat = fun.fatorar(num1)

print(f"O resultado das funções, é: {som,sub,mul,div,fat}")