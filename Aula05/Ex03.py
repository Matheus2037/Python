lista1 = list(range(1, 6))
lista2 = list(range(6, 11))
lista3 = []

print(lista1)
print(lista2)

for i in range(0, 5):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista3)