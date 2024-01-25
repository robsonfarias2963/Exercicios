class Pessoa:
    def __init__(self,nome,sexo,cpf,ativo):
        self.nome = nome
        self.sexo = sexo
        self.cpf  = cpf
        self.ativo = ativo

    def desativar(self):
        self.ativo = False
        print("A pessoa foi desativada com sucesso")
    # retorna o valor o nome
    def get__nome(self):
        return self.__nome
    # atualiza o nome
    def set__nome(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    nome.setter

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

if __name__=="__main__":
    pessoa1 = Pessoa("joao","M","123456",True)
    pessoa1.desativar()
    pessoa1.ativo = True
    print(pessoa1.ativo)

   # utulizando get e setters
    pessoa1.set__nome("jose")
    print(pessoa1.get__nome())

