A,B,C,D=map(int,input().split())

soma1= C+D
soma2=A+B
if B>C and D>A and soma1>soma2 and C>0 and D>0 and A%2==0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
    