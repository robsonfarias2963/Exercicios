palavras = ('Mario','Luigi','Peach','Yoshi','Bowser')

for palavra in palavras:
    print('\nPalavra: {} .vogais:'.format(palavra.upper()), end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end='')