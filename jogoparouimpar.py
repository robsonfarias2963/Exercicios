from random import randint

while True:
    jogador = int(input("Digite um valor:"))
    computador = randint (1,11)
    total= jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo= str(input('Par e Impar ? [P/I]')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}.total e {total}')
    if tipo == 'p':
        if total % 2 == 0:
            print("voçe venceu")
            v += 1
        else:
            print('voçe perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print("voçe venceu")
            v += 1
        else:
            print("voçe perdeu")
            break
    print("Vamos jogar novamente")
    print("GAME OVER! voçe venceu {v} vezes.")