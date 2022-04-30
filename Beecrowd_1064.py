cont=0 
soma=0
for c in range(1,7):
    num=float(input())
    if num >0:
        cont+=1
        soma+=num
print(f'{cont} valores positivos')
print(f'{soma/cont:0.1f}')
        