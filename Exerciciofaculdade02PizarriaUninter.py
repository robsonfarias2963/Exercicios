acumulador=0
acrescimo=0
print(' Programa vendas de Pizza, Robson de farias' )
print ( 'COD === Descricao === Pizza Media-M === Pizza Grande -G(30% de desconto' )
print ( '21 === Napolitana ==== R$ 20,00     ===  R$ 26,00' )
print ( '22 === Margherita ==== R$ 20,00     ===  R$ 26,00' )
print ( '23 === Calabresa  ==== R$ 25,00     ===  R$ 32,50' )
print ( '24 === Toscana    ==== R$ 30,00     ===  R$ 39,00' )
print ( '25 === Portuguesa ==== R$ 30,00     ===  R$ 39,00 ' )

while True :
        tam = bool ( input ( 'Digite o tamanho da pizza desejada (M/G):' ) )
        cod = int ( input ( ' Informe o codigo do sabor desejado :' ) )
        if tam == 'M' and cod == '21' or tam == 'G' and cod == '21':
            acumulador = acumulador + 20
            acrescimo=acumulador-(acumulador*30/100)
            #print('Voce pediu uma pizza Napolitana - G: R$26,00'.format(acrescimo))
            #print('Voce pediu uma pizza Napolitana - M: R$20,00'.format(acrescimo))
        elif tam == 'M' and cod == '22' or tam == 'G' and cod == '22':
            acumulador = acumulador + 20
            acrescimo = acumulador - (acumulador * 30 / 100)
            #print ( 'Voce pediu uma pizza Napolitana - G: R$26,00'.format(acrescimo))
        elif tam =='M' and cod == '23' or tam =='G' and cod =='23':
            acumulador = acumulador + 20
            acrescimo= acumulador-(acumulador*30/100)
            print('Voce pediu uma pizza Margherita - M: R$20,00')
            #print('Voce pediu uma pizza Napolitana - G: R$26,00'.format(acrescimo))
        elif tam =='M' and cod =='24' or tam == 'G' and cod == '24':
            acumulador= acumulador + 20
            acrescimo= acumulador-(acumulador*30/100)
            #print('Voce pediu uma pizza Napolitana - G: R$26,00'.format(acrescimo))
        elif tam=='M' and cod=='25'or tam == 'G' and cod == '25':
            acumulador=acumulador+20
            acrescimo=acumulador-(acumulador*30/100)
            #print('Voce pediu uma pizza Portuquesa  - G: R$39,00'.format(acrescimo))
        else:
            print('Desejas Pedir mais alguma coisa:')
            print('Voce pediu a pizza de {}'.format(cod))
        resposta=input('Deseja mais alguma coisa? (S/N)')
        if resposta == 'S':
            continue
        else:
            print('O valor final da conta {:.2f}'.format(acrescimo,acumulador))
        break
