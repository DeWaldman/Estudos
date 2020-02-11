#O que esse código faz?
#ele adivinha um numero escolhido aleatoriamente, utilizando um algoritmo chamado: algoritmo binario.
#e.g entre 1 e 300, o algoritmo leva apenas 9 passos para descobrir o numero escolhido.

from random import randint
minn = 0
maxx = int (input ())
valor = randint(minn+1, maxx)
fim=False
baixo=False
alto=False
passos = 0

def game(chute):
  global fim
  global alto
  global baixo
  global passos
  if chute == valor: print('Você venceu!');fim = True;baixo = False;alto = False
  elif chute > valor: print('Chute alto');alto = True;baixo = False;fim = False
  elif chute < valor: print('Chute baixo');baixo = True;alto = False;fim = False
  passos+=1

lista = range(minn, maxx+1)

chute = int(len(lista)/2)
print('\nChute =', chute,)
game(chute)

while fim==False:

  # chute < valor
  if baixo:
    minn = lista.index(chute)
    lista = lista[minn:maxx+1]
    minn = 0
    chute = lista[int(len(lista)/2)]

  # chute > valor
  elif alto:
    maxx = lista.index(chute)
    lista = lista[minn:maxx+1]
    chute = lista[int(len(lista)/2)]

  print('\nChute =', chute)
  game(chute)
print('passos: ',passos)
