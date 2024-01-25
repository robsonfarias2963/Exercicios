print('{:=^40}'.format('Lojas Guanabara'))
preco = float(input('Preco das Compras: R$'))
print('''Formas de Pagamentos
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartao
[ 3 ] 2x no cartao 
[ 4 ] 3x ou mais no cartao''')
opcao = int(input('Qual e a opcao:'))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif  opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de {:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 2 / 100)
    totalparc = int(input('Quantas parcelas '))
    parcela = total / totalparc
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc,parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco,total))
