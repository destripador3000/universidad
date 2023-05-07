

acumulador=0
acumulador2=0

for i in range(0,6):
    numero=int(input("Escribe un número: "))  
    if numero>0:
        acumulador += numero
    elif numero < 0:
         acumulador2 += numero   
         

resultado = acumulador + acumulador2

print(resultado)      