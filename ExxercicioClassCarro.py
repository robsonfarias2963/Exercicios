class Carro(object) :
    def __init__(self,estado,nome) :  # Constutor
        self.estado=estado
        self.nome=nome

    def mostrar_informacoes(self) :
        print(f"O carro {self.nome} tem o estado {self.estado}")


bmw=Carro('semi-novo','BMW')
ferrari=Carro(nome='Ferrari',estado='novo')  # Parâmetro passado de forma nomeada
fusca=Carro(estado='usado',nome='Fusca')

bmw.mostrar_informacoes()
ferrari.mostrar_informacoes()
fusca.mostrar_informacoes()