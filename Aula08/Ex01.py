n1 = int(input("Digite a nota: "))
n2 = int(input("Digite a nota: "))
n3 = int(input("Digite a nota: "))

def medias(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

print(f"A média é: {medias(n1, n2, n3)}")