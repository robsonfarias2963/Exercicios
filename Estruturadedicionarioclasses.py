pessoa = {'Nome': 'Hugo','Profissao': 'Programador' ,'Idade': 20}
pessoa ['Nome'] = 'Fabio'
print(pessoa['Nome'])

class Pessoa:
    pass

Hugo = Pessoa()

Hugo.nome = "Hugo"
Hugo.emprego = "Programador"
Hugo.idade = 30

print(Hugo.__dict__)
