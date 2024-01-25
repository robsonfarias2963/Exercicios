from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual-nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Voce ainda nao tem 18 anos.Ainda faltam {} para o alistamento!'.format(saldo))
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(' Voce ja deveria se alistar ha {} anos!'.format(ano))
    print('Seu alistamento foi em {}'.format(saldo))