#sumatoria de números##
numero2 =float(input("Escribe un número y cero para salir: "))
acumulador=0
while numero2 !=0:
    numero2 =float(input("Escribe un número y cero para salir: "))
    
    resultado = numero2+acumulador
    acumulador+=resultado
print("La suma de todos los números es ", acumulador)