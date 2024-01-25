preco = float(input('Qual o preco do produto?: R$'))
novo = preco - (preco * 5/100)
print('O preco que custava R${}, na promocao com desconto de 5% vai custar R${}'.format(preco,novo))