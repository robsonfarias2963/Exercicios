class Pessoa:
    def __init__(self,nome,corolho,idade):
        self.nome=nome
        self.corolho=corolho
        self.idade=idade


class Nome:
    def __init__(self,primeironome,ultimonome):
        self.primeironome=primeironome
        self.ultimonome=ultimonome


minhaPessoa=Pessoa(Nome("Robson","Farias"),"Marrom",40)
print(minhaPessoa.nome.primeironome)
print(minhaPessoa.nome.ultimonome)
print(minhaPessoa.corolho)
print(minhaPessoa.idade)

