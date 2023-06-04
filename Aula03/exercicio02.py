import math

p1x = int(input("Digite um numero: "))
p1y = int(input("Digite um numero: "))

p2x = int(input("Digite um numero: "))
p2y = int(input("Digite um numero: "))

dist =  (p2x - p1x)**2 + (p2y - p1y)**2
dist = math.sqrt(dist)

print("{:.2f}".format(dist))