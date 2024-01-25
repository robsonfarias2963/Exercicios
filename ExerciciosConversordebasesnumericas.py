num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao:
[1] Converter para Binario
[2] converter para Octal
[3] converter para Hexadecimal''')
opcao = int(input('Sua Opcao:'))
if opcao == 1:
    print('{} convertido para BINARIO e igual a {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Octal e igual a {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal e igual {}'.format(num,hex(num)[2:]))
else:
    print('Opcao invalida tente novamente!')