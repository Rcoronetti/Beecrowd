idade=int(input())
calculo_ano = idade//365
calculo_mes=(idade%365)//30
calculo_dia=(idade%365)%30


print('%d ano(s)\n%d mes(es)\n%d dia(s)'%(calculo_ano,calculo_mes,calculo_dia))