estoque = {}
sistema = True
quantidadeTotal = 0
valorTotal = 0
subtotal = 0

while sistema == True:
        
    escolha = int(input("• Cadastrar: Aperte 1"
                      "\n• Atualizar: Aperte 2"
                      "\n• Verificar: Aperte 3"
                      "\n• Listar: Aperte 4"
                      "\n• Remover: Aperte 5"
                      "\n• Sair: Aperte 6 \n"))
    if escolha == 1:

        nome = input("Digite o nome do produto: ")
        preco = int(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))
        quantidadeTotal += quantidade

        item = []
        item.append(preco)
        item.append(quantidade)

        estoque.update({nome : item})

    elif escolha == 2:

        item = input("Qual item será alterado? ")
        estoque.pop(item)

        nome = input("Digite o nome do produto: ")
        preco = int(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))

        item = []
        item.append(preco)
        item.append(quantidade)

        estoque.update({nome : item})

    elif escolha == 3:
        pesquisa = input("Digite o nome do produto para pesquisar: ")
        print(estoque.get(pesquisa))

    elif escolha == 4:
        for nome, item in estoque.items():
            print(f"O produto {nome}, custa: {item[0]} reais, e possui {item[1]} em estoque!")

    elif escolha == 5:
        item = input("Qual item será deletado? ")
        estoque.pop(item)
    
    elif escolha == 6:
        sistema = False


for nome, item in estoque.items():
    subtotal = estoque[nome][0] * estoque[nome][1]
    valorTotal += subtotal

print(f"A quantidade de itens no estoque é igual a {quantidadeTotal}, o valor do estoque é de {valorTotal}")
    