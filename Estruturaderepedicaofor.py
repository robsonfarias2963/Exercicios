#s = 0
#for c in range(0, 4):
 #   n = int(input('Digite um valor:'))
  #  s += n
#print('O somatorio de todos os valores foi {}'.format(s))

#for i in range (10,20):
 #  for j in range (10, 20 , 2):
  #    print('{} + {} = {}' . format(i, j, i + j))
from enum import Enum


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print('I\'m feeling the blues :(')