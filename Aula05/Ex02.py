notasAluno = []
naMedia = []

for i in range(0, 3):
    nota1 = float(input("Digite a nota: "))
    nota2 = float(input("Digite a nota: "))
    nota3 = float(input("Digite a nota: "))
    nota4 = float(input("Digite a nota: "))

    print("Você digitou as 4 notas desse aluno, indo ao proximo...")

    media = (nota1 + nota2 + nota3 + nota4) / 4
    notasAluno.append(media)

for a in notasAluno:

    if a >= 7:
        naMedia.append(a)

print("As médias acima de 7 são de: ", naMedia)