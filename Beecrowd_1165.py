repeticoes=int(input())
cont=0
for a in range(1,repeticoes+1):
    numeros_teste=int(input())
    for c in range(2,numeros_teste):
        if numeros_teste%c==0:
            print(f'{numeros_teste} nao eh primo')
            cont+=1
            break
    else:   
        print(f'{numeros_teste} eh primo')
        