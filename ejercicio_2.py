#Nombres: Juan Esteban Valencia Londoño#
#         Liseth Yurani Ortega Hurtado
#         Julian Alberto Londoño Mesa  
#Profesor(a):Andrea Palomino Salcedo #
#Tecnología en desarrollo de software código: 2724#
#Laboratorio Número 2#
###  Tenis ### 
nombre = input("Escribe el nombre: ")
edad =int(input("¿Cuál es tu edad? "))
meses =int(input("Escribe la cantidad de meses "))
def valor(nombre,edad, meses):
    
    if edad < 12:
        cantidad = meses * 43000
        print("Nombre: ", nombre,"\n","categoría: Infantil","\n","Valor a pagar:", cantidad )
    elif edad >=12 and edad < 18:
        cantidad = meses * 36000
        print("Nombre: ", nombre,"\n","categoría: Juveniles","\n","Valor a pagar:", cantidad )
    else:
        cantidad = meses * 32000
        print("Nombre: ", nombre,"\n","categoría: Mayores","\n","Valor a pagar:", cantidad )



valor(nombre,edad,meses) 


     
