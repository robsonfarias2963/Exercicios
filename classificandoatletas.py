from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento:'))
idade = atual -nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificao mirim')
elif idade <= 14:
    print('Classificacao infantil')
elif idade <= 19:
    print('Classificao junior')
elif idade <= 25:
    print('Classsificao senior')
else:
    print('Classificao master')