def saudacao():
  print("Olá mundo")
  print("Esta é uma função")

def somar(num1, num2):
  soma = num1 + num2 
  return soma

saudacao()

numero1 = int(input("Digite um numero"))
numero2 = int(input("Digite outro numero"))
s = somar(numero1, numero2)

print(s)

