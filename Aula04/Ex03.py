n = int(input("Digite um número para saber se é primo: "))
resultado = 0
divisores = 0
i = 1

if(n > 0):

    if(n != 1):
        while i <= n:
            if n % i == 0:
                divisores = divisores + 1
            i = i + 1
        if(divisores > 2):
            print("Este número não é primo!")
        else:
            print("Este número é primo!")
    else:
        print("O número 1 não é primo!") 
        exit()
else:
        print("Números negativos não são primos!")   