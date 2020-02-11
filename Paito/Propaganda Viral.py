#uma solucao nao tao boa para uns dos problemas da maratona interna da fatec de 2019

def often(itens):
  l = {}
  for i in itens:
    l[i] = 0
  for i in itens:
    l[i]+=1
  return l

lista1 = [4, 7]
lista2 = []
user = int(input())
tag = True
while True:
  for k in lista1:
    lista2.append(k+4)
    lista2.append(k+7)
  result = often(lista2)
  if user in result.values():
    for j in result.items():
      try:
        j.index(user)
        print(j[0])
        tag = False
        break
      except:
        continue
  if not tag:
      break
  lista1=lista2
  lista2 = []
