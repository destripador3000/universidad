monto=float(input("Cuanto vas a ahorrar: "))
ahorros = 0
while monto > ahorros:
    cuota = float(input("Cuanto vas a ahorrar: "))
    ahorros += cuota
print("Hemos llegado a la meta tus ahorros son", ahorros, "y la meta es ", monto)    