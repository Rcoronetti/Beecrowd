horai,minutoi,horaf,minutof=map(int,input().split())
horajogo=0
minutojogo=0
if horai<horaf:
    horajogo=horaf-horai   
if horai>=horaf:
    horajogo=24-(horai-horaf) 
if horai==horaf and minutoi!=minutof:
    horajogo=0           
if minutoi<=minutof:
    minutojogo=minutof-minutoi
else:
    minutojogo=(60-minutoi)+minutof    
if horai<horaf and minutoi>minutof:
    horajogo=(horaf-horai)-1
if horai>horaf and minutoi>minutof:
    horajogo=23-(horai-horaf)  
print(f'O JOGO DUROU {horajogo} HORA(S) E {minutojogo} MINUTO(S)')    