def verificar_numero(n):
    if isinstance(n, float) and int(n) == n and n > 0:
        return True
    else:
        return False

def soma_inteiros_positivos(n):
    if verificar_numero(n) == True:
        soma = 0
        for i in range(1, int(n + 1)):
            if isinstance(i, int) and i > 0:
                soma += i  
        return soma
    else:
        print("O número digitado precisa ser inteiro e positivo! ")

while True:

    x = float(input("Digite um número: "))

    print(soma_inteiros_positivos(x))

    continuar_resposta = float(input("Caso queira continuar aperte 1: "))

    if int(continuar_resposta) != 1:
        break