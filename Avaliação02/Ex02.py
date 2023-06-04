senhas_invalidas = ['1234', '2345', '3456', '4567', '5678', '6789']
cadastrando = True
tentativas = 5

while cadastrando == True:
    senha = input("Digite uma senha númerica para cadastro de até 4 digitos: ")

    if len(senha) < 4: 
        print("A senha tem que ter 4 números ")
    elif len(senha) > 4:
        print("A senha só pode ter 4 números ")
    else:
        for i in senhas_invalidas:
            if senha == i:
                print("A senha não pode ser uma sequência básica de números!")
                break
            elif senha != i:
                print("Senha cadastrada!")
                cadastrando = False
                break

while True: 
    tentativa = input("Digite a sua senha: ")

    if tentativa == senha:
        print("Bem vindo! ")
        break
    else:
        if tentativas > 1:
            tentativas -= 1
            print(f"Senha incorreta! Você possui {tentativas} tentativas!")
        else:
            break
        

