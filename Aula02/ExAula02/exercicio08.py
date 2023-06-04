preco =   float(input("Qual o valor do produto? "))
desconto =  int(input("Digite qual o desconto deste produto: "))

if desconto == 0:

    valorDesconto = preco * 0
    precoDesconto = preco - valorDesconto

    print("Este produto não possui nenhum desconto seu preço fica: {}" .format(preco))

if desconto == 10:

    valorDesconto = preco * 0.1
    precoDesconto = preco - valorDesconto

    print("O produto custava {:.2f}R$," 
          "com um valor descontado de {:.2f}R$,"
          "fica exatamente {:.2f}R$.". format(preco, valorDesconto, precoDesconto))
    
if desconto == 20:

    valorDesconto = preco * 0.2
    precoDesconto = preco - valorDesconto

    print("O produto custava {:.2f}R$," 
          "com um valor descontado de {:.2f}R$,"
          "fica exatamente {:.2f}R$.". format(preco, valorDesconto, precoDesconto))
    
if desconto == 30:

    valorDesconto = preco * 0.3
    precoDesconto = preco - valorDesconto

    print("O produto custava {:.2f}R$," 
          "com um valor descontado de {:.2f}R$,"
          "fica exatamente {:.2f}R$.". format(preco, valorDesconto, precoDesconto))

    