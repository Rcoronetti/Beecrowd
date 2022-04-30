a,b,c=map(float,input().split())
aux=''
if(a >= b):
    aux = c
    c = b
    b = aux
if(b > a):
    aux = b
    b = a
    a = aux
if(c > b):
    aux = c
    c = b
    b = aux
if (b>c and a<b):
    aux=a
    a=b
    b=aux    

if a>=b+c:
        print('NAO FORMA TRIANGULO')
elif a*a==b*b+c*c:
        print('TRIANGULO RETANGULO')
elif a*a>b*b+c*c:
        print('TRIANGULO OBTUSANGULO')
elif a*a<b*b+c*c:
        print('TRIANGULO ACUTANGULO')
if a==b and b==c and c==a:
        print('TRIANGULO EQUILATERO')
if a==b and a!=c or b==c and b!=a or a==c and a!=b:
        print('TRIANGULO ISOSCELES')