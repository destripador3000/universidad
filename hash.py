#Script para generar un hash de contraseñas
#¡¡¡¡¡---Creo que es mejor utilizar un hash para contraseñas---!!!!!

import time

CONTRASEÑA_1= input('Escribe una contraseña...')
encriptacion =str(hash(CONTRASEÑA_1)) 

print(f'tu contraseña es {CONTRASEÑA_1} y tu hash es {encriptacion}')

with open('contrasenas.txt','a') as file:
    file.write(encriptacion +"-----------")
input('press enter...')
print('Espere un momento...')
time.sleep(3)
validacion=input('Ingrese su contraseña...')
encriptacion_2=str(hash(validacion)) 
if encriptacion_2 == encriptacion:
    print('Bienvenido...')
else:
    print('Creo que no es la contraseña')    

input('Presione eneter...')    