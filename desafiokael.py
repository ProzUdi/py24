import funcaokael
contatos = funcaokael.lerContatos()

def fatorial(num1):
    if num1 ==1:
        return 1
    
    return num1 * fatorial(num1 - 1)

num1 = int(input("digite um numero"))


opcao = 0 
while opcao != 3:
    opcao = funcaokael.opcoes()
    if opcao == 1:
        print("Nome - Numero")
        for contato in contatos:
            print(f"{contato}")
    elif opcao == 2:
        contatos.append(funcaokael.addContao())
    elif opcao == 3:
        print("Obrigado por usar o sistema")
    else:
        print("Opcao invalida!")
