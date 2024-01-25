nome = str(input('Qual seu nome'))
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Pedro' or nome== 'Maria' or nome== 'Paulo':
    print('Seu nome e popular no brasil')
elif nome in 'Ana jessica Claudia juliana':
    print('belo nome feminino')
else:
    print('Seu nome e bem normal ')
print('Tenha um bom dia'.format(nome))

