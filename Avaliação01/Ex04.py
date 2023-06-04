valorHora = float(input('Digite quanto você ganha por hora trabalhada: '))
quantidadeHora = float(input('Digite a quantas horas você trabalhou esse mês: '))

salario = valorHora * quantidadeHora

if salario > 2380:
    print('Você ganhou {:.2f} Reais esse mês, você deve declarar IRPF'.format(salario))
elif salario > 0 and salario < 2380:
    print("Você ganhou {:.2f} Reais esse mês, você é isento de IRPF". format(salario))
else: print('Você possivelmente digitou números inválidos! ')