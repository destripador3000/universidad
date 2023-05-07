def encrypt(word, n):
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    fusion =list(zip(letras,numeros))
    for n in word:
        for i,j in zip(letras, numeros):
            word.replace(i,j)
            print(word)

