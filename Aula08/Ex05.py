def soma_limitada(valor1, valor2, limite):
    if valor1 + valor2 > limite:
        return True
    else:
        return False
    
valor1 = float(input("Digite um número: "))
valor2 = float(input("Digite mais um número: "))
limite = float(input("Digite um número limite: "))

print(soma_limitada(valor1, valor2, limite))