from datetime import date
atual = date.today().year
totalmaior = 0;
totalmenor = 0;
for pess in range(1,8):
    nasc = int(input('Em que ano a ´pesssoa nasceu!:'.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1;
print('Ao todo nos tivemos {} pessoas maiores de idade:'.format(totalmaior))
print('Ao todo nos tivemos {} pessoas menores de idade'.format(totalmenor))