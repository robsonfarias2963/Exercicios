class Casa:
    lista = []

    def __init__(self, qtdd_quartos, qtdd_banheiros, qtdd_vagas):
        self.qtdd_quartos = qtdd_quartos
        self.qtdd_banheiros = qtdd_banheiros
        self.qtdd_vagas = qtdd_vagas

        Casa.lista.append(self)

    @classmethod
    def constroi_alto_padrao(cls):
        return cls(qtdd_quartos=5, qtdd_banheiros=5, qtdd_vagas=3)

    @classmethod
    def constroi_popular(cls):
        return cls(qtdd_quartos=1, qtdd_banheiros=1, qtdd_vagas=1)

    def __repr__(self):
        return f'A casa possui {self.qtdd_quartos} quartos {self.qtdd_banheiros} banheiros e {self.qtdd_vagas} vagas.'

    @classmethod
    def filtro_qtdd_quartos(cls, qtdd_quartos):
        lista_casas_filtro = []
        for casa in cls.lista:
            if casa.qtdd_quartos >= qtdd_quartos:
                lista_casas_filtro.append(casa)
            return lista_casas_filtro

    @classmethod
    def filtro_qtdd_banheiros(cls, qtdd_banheiros):
        lista_casas_filtro = []
        for casa in cls.lista:
            if casa.qtdd_banheiros >= qtdd_banheiros:
                lista_casas_filtro.append(casa)
            return lista_casas_filtro

    @staticmethod
    def is_alto_padrao(casa: object) -> object:
        return (casa.qtdd_quartos >= 4)


print(Casa.constroi_alto_padrao())
print(Casa.constroi_popular())
# casa_1 = Casa(qtdd_quartos=2, qtdd_banheiros=3, qtdd_vagas=2)
# casa_2 = Casa(qtdd_quartos=3, qtdd_banheiros=5, qtdd_vagas=4)
# casa_3 = Casa(qtdd_quartos=1, qtdd_banheiros=1, qtdd_vagas=1)
# lista_filtro = Casa.filtro_qtdd_banheiros(qtdd_banheiros=2)
# print(lista_filtro)
# print(Casa.is_alto_padrao(casa_1))
