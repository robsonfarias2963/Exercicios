print('-=' * 20)
print('Analizando o triangulo')
print('-=' * 20)
r1 = float(input('primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triangulos!')
else:
    print('Os segmentos acima nao podem formar triangulos!')