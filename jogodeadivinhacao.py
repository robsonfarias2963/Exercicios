from random import randint
computador = randint(0,5) # faz o computador pensar
print('-=-' * 20)
print('Vou pensar num numero entre 0 e 5. tenta adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei!'))# jogador tenta adivinhar
if jogador == computador:
    print('Parabens voce conseguiu vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e nao no {}!'.format(computador,jogador))