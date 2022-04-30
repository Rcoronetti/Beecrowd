dentro=0
out=0
n=int(input())
for c in range(1,n+1):
    x=int(input())
    if x>=10 and x<=20:
        dentro+=1
    else:
        out+=1
print(f'{dentro} in')        
print(f'{out} out') 