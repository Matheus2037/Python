pagamento = float(input("Digite quanto dinheiro você pode pagar: "))

litros = pagamento / 4.95

distancia = litros * 20

print("Com esse valor é possivel abastecer {:.2f} litros" .format(litros))
print("Com esse combustivél é possivel percorrer {:.2f} Km" .format(distancia))