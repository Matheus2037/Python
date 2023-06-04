escolha = 0
n = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
resultado = 0

while escolha != 5:
    escolha = int(input("• Adição: Aperte 1"
                      "\n• Subtração: Aperte 2"
                      "\n• Multiplicação: Aperte 3"
                      "\n• Divisão: Aperte 4"
                      "\n• Saída: Aperte 5 \n"))
    if escolha == 1:
        resultado = n + n2
        print(f"O resultado da soma é: {resultado}\n")
        escolha = int(input("Continuar - (Pressione qualquer número), Sair - 5\n"))
    elif escolha == 2:
        resultado = n - n2
        print(f"O resultado da subtração é: {resultado}\n")
        escolha = int(input("Continuar - 1, Sair - 5\n"))
    elif escolha == 3:
        resultado = n * n2
        print(f"O resultado da multiplicação é: {resultado}\n")
        escolha = int(input("Continuar - 1, Sair - 5\n"))
    elif escolha == 4:
        resultado = n / n2
        print(f"O resultado da divisão é: {resultado}\n")
        escolha = int(input("Continuar - 1, Sair - 5\n"))
    elif escolha == 5:
        print("Saindo!")
    else: 
        print("O número digitado é inválido! ")
        escolha = int(input("Continuar - 1, Sair - 5\n"))

print("\nVocê saiu do menu") 