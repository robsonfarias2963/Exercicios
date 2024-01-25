velocidade = float(input('Qual a velocidade atual do carro:'))
if velocidade > 80:
    print('Multado voce exedeu o limite permitido que e de 80Km/h')
    multa = (velocidade-80) * 7
    print('Voce deve pagar multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! dirija com seguranca!')