def somar(num1, num2):
    soma = num1 + num2
    return(soma)

def subtrair(num1, num2):
    diminuir = num1 - num2
    return(diminuir)

def multiplicacao(num1, num2):
    multiplicar = num1 * num2
    return(multiplicar)

def divisao(num1, num2):
    dividir = num1 / num2
    return(dividir)

def fatorial(num):
    fatorar = 1
    while num > 1:
        fatorar = fatorar * num
        num = num - 1
    return fatorar    

#funçao recursiva <<<
# def fatorial (num):
#   if ( num == 1):
#     return num 1
#return num * fatorial(num - 1)
 
#outra forma de fazer função divisão<<<
# def dividir(num1, num2):
    # if num2 == 0:
    #     return "Não é possível dividir por zero"
    # else:
    #     return num1 / num2

# para testar as funções