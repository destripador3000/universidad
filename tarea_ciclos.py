num = int(input("Escribe un número: "))
for i in range(num,0,-1):
    for n in range(i):

        print(i," ",end="")
        i-=1
    print()
    
       