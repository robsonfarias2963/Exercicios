import math

class Point:
    'aqui representa um ponto em duas dimensoes geometrica.'

    def __init__(self,  x=0 ,  y=0):
        'inicializa um novo ponto x e y.'

        self.move(x,y)

    def move(self,x,y):
        ' movera um ponto pra uma nova locaçao  em 2 espaço.'
        self.x = x
        self.y = y

    def reset(self):
        'reseta o ponto atras para a geometria original.'
        self.move(0,0)

    def calcula_distancia(self,outro_ponto):
        ' calcula a distancia desse ponto para o segundo ponto passando como parametro.'

        ' esta funcao usa um teorema pythagorean para calacular a distancia entre dois pontos.retornando como floato valor'
        return math.sqrt((self.x - outro_ponto.x)**2 + (self.y - outro_ponto.y)**2)
point1 = Point()
point2 = Point()

point1.reset
point2.move(8,2)
print(point2.calcula_distancia(point1))
assert (point2.calcula_distancia(point1)== point1.calcula_distancia(point2))
point1.move(7,4)
print(point1.calcula_distancia(point2))
print(point1.calcula_distancia(point1))