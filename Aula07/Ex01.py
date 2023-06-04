rep = 0
lista = []

while rep != -1:
    n = int(input("Digite um número postivo: "))
    if n >= 0: 
        lista.append(n)
    elif n == -1:
        rep = -1
    else: 
        print("Se deseja sair aperte '-1'")

print("A soma de todos os números positivos digitados é =", sum(lista),'.')
print("A média de todos os números positivos digitados é =", sum(lista)/len(lista),'.')
print("O maior número positivo digitado é =", max(lista),'.')
print("O menor número positivo digitado é =", min(lista),'.')