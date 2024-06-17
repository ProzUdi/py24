def saudacao():
    print("Olá mundo")
    print("Esta é uma função")

saudacao() #<< CHAMANDO A FUNÇÃO<<

def somar(num1, num2):
    soma = num1 + num2
    return(soma)

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: " ))

s = somar(numero1, numero2)
print(s)