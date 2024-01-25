temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))  # Convertendo o peso para float
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'Os dados foram {princ}.')
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi {mai}kg.')
print(f'O menor peso foi {men}kg.')
