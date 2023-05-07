
#Script que busca archivos con una determinada ruta
import pathlib

lista = []
ruta = pathlib.Path('.')

for archivo in ruta.glob('*.txt'):
    lista.append(archivo)
    
    
    
    print(archivo)
    str(archivo)
    print(type(archivo))  
    print(lista)  
input('Press enter...')
