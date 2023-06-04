mesEscrito = ""

while True:

    data = input("Digite uma data no formato DD/MM/AAAA: ")

    dia = data[:2]
    mes = data[3:5]
    ano = data[6:]

    if not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
            print("A data digita contém caracteres inválidos!")
            break
    
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1:
        print("Algum valor digitado excede o valor máximo!")
        break

    if mes in [4, 6, 9, 11] and dia > 30:
        print("O mês digitado só vai até o dia 30!")
        break
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            if dia > 29:
                print("Durante o ano digitado Fevereiro só tem 29 dias!")
                break
        elif dia > 28:
            print("Durante o ano digitado Fevereiro só tem 28 dias!")
            break
    
    match mes:
        case 1:
            mesEscrito = "Janeiro"
        case 2:
            mesEscrito = "Fevereiro"
        case 3:
            mesEscrito = "Março"
        case 4:
            mesEscrito = "Abril"
        case 5:
            mesEscrito = "Maio"
        case 6:
            mesEscrito = "Junho"
        case 7:
            mesEscrito = "Julho"
        case 8:
            mesEscrito = "Agosto"
        case 9:
            mesEscrito = "Setembro"
        case 10:
            mesEscrito = "Outubro"
        case 11:
            mesEscrito = "Novembro"
        case 12:
            mesEscrito = "Dezembro"

    print("*"*50)
    print("\n")
    print(f"Dia {dia} de {mesEscrito} de {ano}")
    print("\n")
    print("*"*50)