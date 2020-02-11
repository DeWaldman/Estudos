file = open('numeros.txt', 'r')
for linha in file.readlines():
  print(linha,end='')
file.close()

#linha.rstrip() retira os caracteres de controle da direita daquela linha

#with open('numeros.txt') as f:
#  print(f.read())
