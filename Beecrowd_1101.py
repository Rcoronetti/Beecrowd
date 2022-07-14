'''Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até
 o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.'''

n=1
m=1
soma=0
while n>0  and m>0:
    n,m=map(int,(input().split()))    
    if n<=0 or m<=0:
        break
    if n>=m:
        soma=0
        for c in range(m,n+1):
            soma+=c            
            print(f'{c}',end=' ')
        print(f'Sum={soma}')           
            
       
    else:   
        soma=0
        for c in range(n,m+1):
            soma+=c  
            print(f'{c}',end=' ')
        print(f'Sum={soma}')
            
