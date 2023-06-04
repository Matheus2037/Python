preco = float(input("Qual o valor do produto? "))

valorDesconto = preco * 0.2
precoDesconto = preco - valorDesconto

print("O produto custava {:.2f}R$, com um valor descontado de {:.2f}R$, fica exatamente {:.2f}R$.". format(preco, valorDesconto, precoDesconto))