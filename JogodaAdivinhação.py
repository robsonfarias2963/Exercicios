from random import randint
computador = randint(1,10)
print('Sou seu computador .... Acabei de pensar em um numero de 0 a 10.')
print('Sera que voçe conseguiu adivinhar qual foi.')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite.'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ... Tente mais uma vez!')
        elif computador > jogador:
            print('Menos ... Tente mais uma vez')
print('Acertou com {} tentativas'.format(palpites))