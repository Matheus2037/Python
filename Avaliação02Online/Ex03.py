atleta = input("Digite o nome do atleta: ")
notas = []

for i in range(0,7):

    nota = float(input("Digite a nota: "))
    notas.append(nota)

menorNota = min(notas)
maiorNota = max(notas)

notas.remove(menorNota)
notas.remove(maiorNota)

media = sum(notas) / len(notas)

print(f"Atleta: {atleta}"
    f"\nMaior nota: {maiorNota}"
    f"\nMenor nota: {menorNota}"
    f"\nSua média foi: {media:.2f}")