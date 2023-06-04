altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso atual: "))
sexo = int(input("Digite seu sexo: 1 - Mulher, 2 - Homem "))


if sexo == 1:
    pesoIdeal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal seria {pesoIdeal:.2f}, você está atualmente com {peso}")
elif sexo == 2:
    pesoIdeal = (72.7 * altura) - 58
    print(f"Seu peso ideal seria {pesoIdeal:.2f} quilos, você está atualmente com {peso} quilos")
else:
    print("O sexo digitado é inválido!")

