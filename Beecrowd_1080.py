cont=0
maior=0
contmaior=0
while cont <100:
    cont+=1
    valor=int(input())
    if valor>maior:
        maior=valor
        contmaior=cont
print(maior)
print(contmaior)    