def somar(num1, num2):
    return(num1 + num2)

def subtrair(num1, num2):
    return(num1 - num2)

def multiplicar(num1, num2):
    return(num1 * num2)

def dividir(num1, num2):
    if (num2 == 0):
        print("Não pode fazer divisão por zero!")
        return(0)
    else:
        return(num1 / num2)

def fatorar(num1):
    fat = 1
    while num1 > 1:
        fat = fat * num1
        num1 -= 1
        
    return(fat)

def fatorial_recursiva(num):
    if (num == 1):
        return(1)
    return(num * fatorial_recursiva(num-1))