import math

raio = int(input("Qual o valor do raio desse circulo? "))

perimetro =  2 * math.pi * raio
area = math.pi * raio ** 2

print("O perimetro dessa circunfêrencia é de {:.2f}, e sua area é de {:.2f}" .format(perimetro, area))