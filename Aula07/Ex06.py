#Os exercicios estão misturados, irei continuar corretamente a partir desse, corresponde ao exercicios 10.


x = int(input("Digite um número: "))
y = int(input("Digite um número maior: "))
lista = []
cont = 0

if x < y:

    cont = cont + x

    while cont != y + 1:
        lista.append(cont)
        cont += 1 
        
print(lista)