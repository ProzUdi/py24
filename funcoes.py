def somar(num1, num2):
  return num1 + num2

def subtrair(num1, num2):
  return num1 - num2

def multiplicar(num1, num2):
  return num1 * num2

def dividir(num1, num2):
  if (num2 == 0):
    print("Não pode fazer divisão por zero")
    return 0
  
  return num1 / num2

def fatorial(num):
  if (num == 1):
    return 1
  
  return num * fatorial(num -1)