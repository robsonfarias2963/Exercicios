somaidade = 0;
mediaidade = 0;
maioridadehomem = 0;
nomevelho = '';
totalmulher20 = 0;
for p in range (1,5):
    print('------ {}" Pessoa ------'.format(p))
    nome = str(input('NOME:')).strip()
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO  M/F')).strip()
    somaidade  += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho =   nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
mediaidade = idade /4
print('A media de idade do grupo e de {} anos:'.format(mediaidade))
print('A idade do homen mais velho e {} anos :'.format(maioridadehomem,nomevelho))
print(' A idade da mulher menores de vinte  {} anos:'.format(totalmulher20))