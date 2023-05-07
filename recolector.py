#Script encargado de recoger toda información posible del administrador

usuarios=int(input('¿Cuantos usuarios vas a ingresar? '))
datos=[]
for i in range(usuarios):
    correo=input('Ingresa tu correo: ')
    numero=int(input('Ingrese su número de celular: '))
    nombre=input('Ingrese su nombre: ')
    cuenta=int(input('Ingrese número de la cuenta: '))
    contraseña=input('Ingrese la contraseña: ')
        

    datos.append(correo)
    datos.append(numero)
    datos.append(nombre)
    datos.append(cuenta)
    datos.append(contraseña)
print(f'Estos fueron los datos entregados: {datos}')
input('Presione entener para continuar...')
    
