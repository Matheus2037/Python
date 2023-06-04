i = 1
contPar = 0

for cont in range(0,5):
    num = int(input("Digite algum número: "))
    if num % 2 == 0:
        print("Este número é par!")
        contPar += 1
    else:
        print("Este número não é par!")
print(f"A quantidade de números pares é de: {contPar}")
