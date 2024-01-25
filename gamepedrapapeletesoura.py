from random import randint
from time import sleep

itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print(''' Suas Opcoes:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura ''')
jogador = int(input('Qual a sua jogada:'))
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('JO')
sleep(1)
print('ken')
sleep(1)
print('PO!!')
print('-=' * 11)
if computador == 0: # jogador jogou pedra
    if jogador == 0:
        print('Empate')

    elif jogador == 1:
        print('Jogador vence')

    elif jogador == 2:
        print('Computador vence')

    else:
        print('Jogada invalida!')

elif computador == 1: # jogador jogou papel
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('vence')

    elif jogador == 2:
        print('jogador vence')
    else:
        print('Jogada invalida!')

elif computador == 2: # jogador jogou tesoura
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada invalida!')