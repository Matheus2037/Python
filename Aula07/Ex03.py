#Os exercicios estão misturados, irei continuar corretamente a partir desse, corresponde ao exercicios 07.


groceries = {} #Criando um dicionário vazio.
total = 0

while True:    #Contador principal.

    cod = int(input("Digite o código do produto: ")) #Coleta dos dados dos produtos.
    name = input("Digite o nome do produto: ")
    price = float(input("Digite o preço do produto: "))
    quantity = int(input("Digite a quantidade desse produto: "))

    info = []  #Criação de uma lista para armazenar os valores, para depois unir com a chave.
    info.append(name)
    info.append(price)
    info.append(quantity)

    groceries.update({cod: info}) #Update no dicionário que estava vazio com a chave e a lista que contém os valores.

    answer = int(input("Deseja continuar? 1-SIM, 2-NÃO: "))  #Decisão se irá continuar a compra.
    if answer == 2:
        break

for cod, info in groceries.items():  #Estrutura na qual "cod" e "info" assumirão os valores dentro dos itens do dicionário

    subtotal = groceries[cod][1] * groceries[cod][2] #Subtotal faz a conta entre o valor e a quantidade do produto.
    #Onde groceries[cod][1] está acessando o primeiro item do dicionário pelo cod assumido na estrutura de reptição ]
    # e dentro da lista está pegando o item 1 correspondente ao valor, multiplicando com o item 2 sendo a quantidade.
    print(f"O produto {info[0]}, custou: {subtotal:.2f}")

    total = total + subtotal

print(f"O total das suas compras foi de: {total}")