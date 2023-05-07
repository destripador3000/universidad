##Tabla de multiplicar###
numero =int(input("Escribe el Número: "))

acumulador= 0
while numero != 0 and acumulador <=10:
    acumulador+=1
    
    resultado =acumulador*numero
    print("La tabla de multiplicar es ",numero,"X", acumulador,"=", resultado )
