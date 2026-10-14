monto = int(input("Monto a retirar: "))
billetes_10000 = monto // 10000
resto = monto % 10000
billetes_5000 = resto // 5000
resto = resto % 5000
billetes_1000 = resto // 1000
resto = resto % 1000
print("Billetes de 10 000:", billetes_10000)
print("Billetes de 5 000:", billetes_5000)
print("Billetes de 1 000:", billetes_1000)
print("Monto no entregado:", resto)