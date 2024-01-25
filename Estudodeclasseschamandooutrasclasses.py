class Animal:
    def __init__(anim,cor ,genero,andar):
        anim.cor =cor
        anim.genero = genero
        anim.num_de_patas = andar

    def falar(anim):
        print("Ola sou um cachorro e sei falar")

    def andar(anim):
        print("Estou andando sobre {} patas".format(anim.num_de_patas))

    def amamentar(anim):
        if anim.genero.lower() [0] == 'm':
            print('Machos nao amamentam')
            return
        print('Amamentando meus filhotes')

#Rex = Animal('marrom','macho',4)
#Rex.falar()
#Rex.andar()
#Rex.amamentar()

class Pessoa(Animal):
    def __init__(anim,cor,genero,andar,cabelo):
        super(Pessoa,anim).__init__(cor,genero,andar)
        anim.cabelo = 'Castanho'

    def falar(anim):
        super(Pessoa,anim).falar()
        print("Ola sou uma pessoa e sei falar")
Hugo = Pessoa('branco','Masculino',2,'Castanho')
Hugo.falar()
