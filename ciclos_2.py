##Tablas de multiplicar##
num=int(input("Escribe el valor de la tabla de multiplicar"))
contador=1

print("la tabla del  " + str(num)+ "es: ")
for i in range(0,10,1):
    resultado = num * contador
    print(str(num)+ " X " + str(contador)+ " es igual a: ", resultado)
    contador+=1  