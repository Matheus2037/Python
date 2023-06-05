def verificar_ano_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
ano_verificar = int(input("Digite um ano para verificar se é bissexto: "))

print(verificar_ano_bissexto(ano_verificar))