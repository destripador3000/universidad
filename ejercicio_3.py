#Nombres: Juan Esteban Valencia Londoño#
#         Liseth Yurani Ortega Hurtado
#         Julian Alberto Londoño Mesa  
#Profesor(a):Andrea Palomino Salcedo #
#Tecnología en desarrollo de software código: 2724#
#Laboratorio Número 2#
##Función de calcular la variable##
x= int(input("Escribe el valor de la variable: "))
def valores_f(x):
    if x <= 0:
        resultado = 8 * (x**2) -6
        print("Resultado: ", resultado)
    elif x > 0:
        resultado2 = 3 * x+5
        print("Resultado: ", resultado2)
    else:
        print("Error, opción no válida")

valores_f(x)
  