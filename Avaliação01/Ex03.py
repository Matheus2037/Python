nr = float(input('Digite algum número: '))

if nr < 0:
    print(f"O número digitado é negativo: {nr}")
elif nr > 0:
    print(f"O número digitado é positivo: {nr}")
else:
    print(f"O número digitado é igual a zero: {nr}")