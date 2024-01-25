class Carros():
    def __init__(self,nome,cor):
        self.nome =nome
        self.cor = cor
    def descricao(self):
        print(f'O carro : {self.nome} e {self.cor}')

class Gol(Carros):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

class Corsa(Carros):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

gol1 = Gol("Gol2019Completo","Branco")
corsa1=Corsa("corsa 2017 2 portas","vermelho")

print(gol1.descricao())
print(corsa1.descricao())
