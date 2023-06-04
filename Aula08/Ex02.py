n1 = float(input("Digite a nota: "))
n2 = float(input("Digite a nota: "))
n3 = float(input("Digite a nota: "))


def medias(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

media = medias(n1, n2, n3)

def verificarStatus(media):
    
    if media >= 6:
        print("Aprovado")
    elif media >= 4 and media< 6:
        print("Verificação Suplementar")
    elif media < 4:
        print("Reprovado")
  
verificarStatus(media)