peso =   float(input('Digite o seu peso em quilos: ' ))
altura = float(input('Digite a sua altura em metros: '))

Imc = peso / altura ** 2

if Imc > 0 and Imc < 18.5:
    print('Você está atualmente abaixo do peso! Seu imc é de: {:.2f}' .format(Imc))
elif Imc >= 18.5 and Imc < 25: 
    print('Você está com o peso normal! {:.2f}' .format(Imc))
elif Imc >= 25 and Imc < 30: 
    print('Você está atualmente com sobrepeso! {:.2f}' .format(Imc))
elif Imc >= 30 and Imc < 35: 
    print('Você está atualmente com obesidade grau 1! {:.2f}' .format(Imc))
elif Imc >= 35 and Imc < 40: 
    print('Você está atualmente com obesidade grau 2! {:.2f}' .format(Imc))
elif Imc > 40: 
    print('Você está atualmente com obesidade grau 3! {:.2f}' .format(Imc))
else: 
    print("Você provavelmente digitou um valor inválido! ")