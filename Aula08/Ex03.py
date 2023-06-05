def imprimir_funcionario(nome, salario=9000):
    print("Nome do funcionário:", nome)
    print("Salário do funcionário:", salario)

while True:

    funcionario_nome = input("Digite o nome do funionário: ")
    funcionario_salario = int(input("Digite o salario do funionário: "))

    imprimir_funcionario(funcionario_nome, funcionario_salario)

    continuacao_resposta = int(input("Digite 1 caso queira continuar: "))

    if continuacao_resposta != 1:
        break