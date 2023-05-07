#from cryptography.fernet import Fernet
#import pathlib

from cryptography.fernet import Fernet
import os

ruta="C:\\Users\\juane\\OneDrive\\Escritorio\\encrypted"

lista=[]

enlistar=os.listdir(ruta)

val =Fernet.generate_key()

ll =Fernet(val)

print(enlistar)

for i in enlistar:
    if i.endswith('.txt'):
        xxx=i.encode('utf-8')
        criptografer = ll.encrypt(xxx)
        
        lista.append(xxx)
        print(lista) 
        
        print(criptografer)
input('press enter...')        
