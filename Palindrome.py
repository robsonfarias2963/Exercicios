frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
     inverso += junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print(" E palindrome!:")
else:
    print('Nao e palindrome!:')
