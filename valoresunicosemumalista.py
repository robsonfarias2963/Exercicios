numeros = list()
while True:
    n = int(input('digite um valor:'))
    if n not in numeros:
        numeros.append(n)
        print('valor adicionado com sucesso')
    else:
        print('valor duplicado! nao vou adicionar')
    r =str(input('quer continuar! [S/N]'))
    if r in 'Nn':
        break
print('-=' *30)
numeros.sort()
print(f'voce digitou os valores{numeros}')
