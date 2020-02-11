#Desafio Criado por Reinaldo Arakaki (Fatec São José dos Campos) | Adaptado por erich.rodriguesf | Competição: Interfatecs 2014 2ª fase
#https://ucoder.com.br/problems/1019/

l1=list(input())
l2=list(input())
l3=list(input())
l4=list(input())
l5=list(input())
matrix = [l1,l2,l3,l4,l5]
estagios = 1
def show(estagios):
  print(''.join(matrix[0]))
  print(''.join(matrix[1]))
  print(''.join(matrix[2]))
  print(''.join(matrix[3]))
  print(''.join(matrix[4]))
  print()

def contaminado(y,x):
  mudou = False
  pontos = 0;
  if x!=4 and matrix[y][x+1] == '1' and matrix[y][x]!='1': pontos += 1
  if x!=0 and matrix[y][x-1] == '1' and matrix[y][x]!='1': pontos += 1
  if y!=0 and matrix[y-1][x] == '1' and matrix[y][x]!='1': pontos += 1
  if y!=4 and matrix[y+1][x] == '1' and matrix[y][x]!='1': pontos += 1
  if pontos>=2:fut_matrix.append([y,x]); mudou = True
  return mudou
  
def matrizes():
  loop = False
  for y in range(5):
    for x in range(5):
      mudou = contaminado(y,x)
      if mudou: loop = True
  for p in fut_matrix: matrix[p[0]][p[1]] = '1'
  return loop

loop = True
while loop:
  fut_matrix = []
  loop = matrizes()
  estagios += 1
  
show(estagios)
