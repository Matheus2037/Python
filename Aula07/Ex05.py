#Os exercicios estão misturados, irei continuar corretamente a partir desse, corresponde ao exercicios 09.

coolaboradores = { 1 : 'Matheus', 2 : 'Domingos', 3 : 'João', 4 : 'zé'}

escolhido = int(input("Digite o ID do funcionário a ser demitido: "))

if escolhido > len(coolaboradores):
    print("O ID de funcionário digitado ainda não foi utilizado: ")
elif escolhido <= 0:
    print("O ID digitado é inválido! ")
else:
    del coolaboradores[escolhido]

print("Os funcionários restantes são:",coolaboradores)