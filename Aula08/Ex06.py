lista = []
valor_minimo = 5

def procura_numero_lista(args, n):
    for i in args:
        if i == n:
            return True
    return False

while True:  
    n_lista = float(input("Digite um número para por na lista: "))
    lista.append(n_lista)
    if len(lista) == valor_minimo:
        continuar_resposta = int(input("Se deseja continuar pressione 1: "))
        if continuar_resposta != 1:
            break
        else:
            valor_minimo += 5

n = float(input("Qual número deve ser procurado na lista? "))
if procura_numero_lista(lista, n) == True:
    print("o número digitado está dentro dessa lista!")
else:
    print("O número digitado não está dentro da lista!")