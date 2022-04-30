salario = float(input('digite o salario'))
salario2 = ((salario-2000.00) *0.08)
salario3 = ((salario-3000.00)*0.18)+(1000.00*0.08)
salario4 = ((salario-4500.00)*0.28)+(1500.00*0.18)+(1000.00*0.08)
if salario <=2000.00:
    print('Isento')
elif salario > 2000.00 and salario <=3000.00:
    print('R$ %0.2f'%(salario2))
elif salario >3000.00 and salario <=4500.00:
    print('R$ %0.2f'% (salario3))
else:
    print('R$ %0.2f'%(salario4))

    