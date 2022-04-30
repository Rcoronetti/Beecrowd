a,b,c=input().split()
a,b,c = [int (a), int (b) , int(c)]

if a>b and a>c:
    print('%d eh o maior'%a)
elif b>a and b>c:
     print('%d eh o maior'%b)
else:
     print('%d eh o maior'%c)