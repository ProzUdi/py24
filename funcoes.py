def somar (num1,num2):
    soma = num1 + num2
    return soma 

def subtrair(num1,num2):
    subtracao = num1 - num2
    return subtracao

def multiplicar(num1,num2):
    multiplicacao = num1 * num2
    return multiplicacao


def dividir (num1,num2):
    if(num2 == 0):
        print("nao pode fazer divisao por zero")
        return 0 
    divisao = num1 / num2
    return divisao


def fatorial(num):
    fat = 1 
    while num > 1 :
        fat = fat *num
        num = num -1
        return fat 
    