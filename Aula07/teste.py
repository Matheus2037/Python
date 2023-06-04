def verificar_data(data):
    # Verifica se a data tem o formato correto
    if len(data) != 10 or data[2] != '/' or data[5] != '/':
        return False

    # Separa o dia, mês e ano da data
    dia, mes, ano = data[:2], data[3:5], data[6:]

    # Verifica se o dia, mês e ano são numéricos
    if not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
        return False

    # Verifica se o dia, mês e ano estão dentro dos limites válidos
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1:
        return False

    # Verifica se o dia é válido para o mês específico
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            if dia > 29:
                return False
        elif dia > 28:
            return False

    return True

# Recebe a data do usuário
data = input("Digite uma data no formato DD/MM/AAAA: ")

# Verifica se a data é válida
if verificar_data(data):
    print("A data é válida!")
else:
    print("A data é inválida!")
