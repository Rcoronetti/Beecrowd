x=int(input())
y=int(input())
a=0
b=0
soma=0
if x>y:
    b=x
    a=y
    for c in range(a,b+1):
        if c%13!=0:
            soma+=c  
             
else:
    for c in range(x,y+1):
        if c%13!=0:
            soma+=c   
print(soma)