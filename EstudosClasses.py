class Meu_Objeto :
    def __init__(pessoa,nome,idade) :
        pessoa.nome=nome
        pessoa.idade=idade
        print('Chamando o construtor')

    def imprime(pessoa) :
        print('Ola meu nome e {} eu tenho  {} anos'.format(pessoa.nome,pessoa.idade))


joao=Meu_Objeto("joao","30")
joao.imprime()
