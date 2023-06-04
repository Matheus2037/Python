#Os exercicios estão misturados, irei continuar corretamente a partir desse, corresponde ao exercicios 08.

d = {}

while True:

    nome =         input("Digite o nome: ")
    idade =    int(input("Digite a idade: "))
    endereco =     input("Digite o endereço: ") 
    telefone = int(input("Digite o telefone: "))

    dados = []
    dados.append(idade)
    dados.append(endereco)
    dados.append(telefone)
    d.update({ nome: dados })

    rep = int(input("Deseja continuar? 1-SIM, 2-NÃO: "))
    if rep == 2: 
        break

for nome, dados in d.items():
    print(nome,"possui", d[nome][0], "anos e mora em", d[nome][1], "seu telefone é:", d[nome][2])
