print('Bem vindo a exercio da loja: Robson de farias')
valorUnitarioproduto = float(input('Digite o valor do produto:'))
quantiProduto = int(input('Entre quantidade do produto:'))
totalproduto  = valorUnitarioproduto * quantiProduto
if  quantiProduto < 4:
    valorfinal = totalproduto - totalproduto * 0.00 # desconto de 0.00
elif 5 <= quantiProduto  < 19:
    valorfinal =  totalproduto - totalproduto * 0.03 # desconto de 0.03
elif 20 <= quantiProduto < 99:
    valorfinal = totalproduto  - totalproduto  * 0.06 # desconto de 0.06
else:
    valorfinal =  totalproduto  - totalproduto  * 0.10 # desconto de 0.10
print('O valor do produto: {}'.format(totalproduto))
print('O valor do desconto e: {}'.format(valorfinal))

