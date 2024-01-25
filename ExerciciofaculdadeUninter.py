total = 0
dinheiro = 0

while True:
    idade = input('Qual sua idade:')
    if idade == 'sair':
        break
    idade = int(idade)
    total += 1
    if idade < 3:
        ingresso = 0
    else:
         if idade > 12:
             ingresso = 30
         else:
             ingresso = 15
    dinheiro += ingresso

media = dinheiro / total
print('total de pessoas: {}'.format(total))
print('total de arrecadado: {}'.format(dinheiro))
print('Media arrecadada: {}'.format(media))