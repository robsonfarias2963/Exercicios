#for i in range(1,6,1):
 #   print(i)

 #### Exercicio usando For media

soma = 0
qtd = 0
for i in range(1,101):
    if (i % 2 == 0):
        soma += i
        qtd  += 1
media = soma / qtd
print('A media e {}'.format(media))