def somar(num1, num2):
   return num1 + num2
    
def subtrair(num1, num2):
    return num1 - num2
   
def multiplicar(num1, num2):
 return num1 * num2
   
   
def dividir(num1, num2):
    if (num2 == 0):
       print("Não há divisão por zero")
       return 0
    return num1 / num2
   
def fatorial(num):
    fat = 1
    while num > 1:
        fat = fat * num
        num -=1
    return fat
                
                 
