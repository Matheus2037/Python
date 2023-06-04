n = int(input("Digite um número inteiro e positivo: "))

if n > 0:

    while n != 0:
        n -= 1
        print(f"Número: {n}")

else: 
    print("O número digitado não é inteiro ou positivo")