peso =float(input('Qual o seu peso (KG)'))
altura = float(input('Qual a sua altura (m)'))
imc = peso / (altura ** 2)
print('O imc dessa pessoa e de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso normal')
elif  18.5 <=  imc < 25:
    print('Parabens vc esta no peso normal')
elif  25 <= imc < 30:
    print('Voce esta em sobrepeso')
elif 30 <= imc < 40:
    print('voce esta em Obesidade ')
elif imc >= 40:
    print('Voce esta em Obesidade Morbida cuidado')
