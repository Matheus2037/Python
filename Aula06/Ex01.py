p1 = (5.7, 7.8, 9.3, 4.2, 8.0)
p2 = (5.8, 5, 9.1, 4.7, 8.5)

media1 = 0
media2 = 0

for i in p1:
    media1 = media1 + i

for i in p2:
    media2 = media2 + i

media1 = media1/len(p1)
media2 = media2/len(p2)

print("A média da turma 1 é de: ", media1)
print("A média da turma 2 é de: ", media2)

if media1 > media2: 
    print("A maior média é a da turma 1!")

elif media2 > media1:
    print("A maior média é a da turma 2!")
else:
    print("As médias são iguais!")