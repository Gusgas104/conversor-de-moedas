real = float(input('Quanto você tem na sua carteira? R$ '))
dolar = real / 5.47
euro = real / 6.34
pesoargentino = real / 0.0040
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €${:.2f}'.format(real, euro))
print('Com R${:.2f} você pode comprar ARS${:.2f}'.format(real, pesoargentino))