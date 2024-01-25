n1 =int(input('Um valor :  '))
n2 =int(input('Outro valor:  '))
s = n1+n2
m = n1* n2
d = n1 /n2
di = n1 //n2
e = n1 ** n2
print('A soma {} \n o produto e {} \n e a divisao e {:.2f} '.format(s,m,d), end='')
print('Divisao inteira {} e Potencia {}'.format(di,e))