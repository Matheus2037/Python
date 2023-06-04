nr1 = float(input('Digite o primeiro número: '))
nr2 = float(input('Digite o segundo número:  '))

if nr1 < nr2:
    print(f"O menor número é o primeiro: {nr1}")
elif nr1 > nr2:
    print(f"O menor número é o segundo: {nr2}")
else:
    print("Os números digitados são iguais! ")