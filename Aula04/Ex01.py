num = 0
total = 0
media = 0
contador = 0
nrMaior = 0
nrMenor = 0

while (num != -1):
    num = int(input("Digite algum número positivo para acrescentar, ou -1 para cancelar: "))
    if(num > 0): 
        total = total + num
        contador += 1
        media = total / contador
        if (contador < 2):
            nrMenor = num
        if (num > nrMaior):
            nrMaior = num
        elif(nrMenor > num):
            nrMenor = num
        else:
            nrMaior = nrMaior
            nrMenor = nrMenor

print("-" * 128)
print("\n")

print("A soma do números digitados é de: {}, e a média dos números digitados é de: {:.2f}" .format(total, media))
print("O maior número digitado foi: {}, e o menor foi: {}." .format(nrMaior, nrMenor))

print("\n")
print("-" * 128)