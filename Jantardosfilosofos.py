from threading import Thread
from random import uniform
from time import sleep


class Filosofo(Thread):
     def __init__(self, nome, garfoEsq, garfoDir):
           Thread.__init__(self)
           self.nome = nome
           self.garfoDir = garfoDir
           self.garfoEsq = garfoEsq

     def run(self):
         while True:
           sleep(uniform(2, 3))
           print(f'> {self.nome}: estou PENSANDO')
           self.janta()

     def janta(self):
         global garfos
         while True:
           sleep(uniform(5, 10))
           esquerda = garfos[self.garfoEsq]
           if esquerda == 0:
              garfos[self.garfoEsq] = self.nome
              print(f'> {self.nome}: Peguei o garfo da ESQUERDA')
              sleep(uniform(1, 3))
              direita = garfos[self.garfoDir]
              if direita == 0:
                garfos[self.garfoDir] = self.nome
                break
              else:

  # Programa 112 – Jantar dos filósofos.
  #Na linha 6, iniciamos a classe Filosofo instanciando
 #uma thread. Na linha 53, criamos um vetor com os 5 talheres,
#preenchemos com zero, e é nele que vamos fazer o controle de
#quem está usando os talheres. A medida em que um filósofo pega
                 print(f'> {self.nome}: O garfo da DIREITA está com '
                    f'{direita}, soltei o da ESQUERDA')
                 garfos[self.garfoEsq] = 0
           else:
                 print(f'> {self.nome}: Tentei pegar o garfo da '
                 f'ESQUERDA, mas está com {esquerda}')
                 return

         self.jantando()
         garfos[self.garfoDir] = 0
         garfos[self.garfoEsq] = 0

     def jantando(self):
       print(f'> {self.nome}: peguei o garfo da DIREITA, e '
       f'COMECEI a comer')
       sleep(uniform(5, 10))
       print(f'> {self.nome} Terminei de comer, e soltei os garfos')

if __name__ == '__main__':
     garfos = [0] * 5
     nomes = ['Aristoteles', 'Kant', 'Platao', 'Socrates', 'Russel']
     filosofos = []

     for i, nome in enumerate(nomes):
         fil = Filosofo(nome, i - 1, i)
         filosofos.append(fil)

     for f in filosofos:
         f.start()