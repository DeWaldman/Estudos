def hack(n):
  lista = []

  def conta_uns(x):
    return x.count('1')#retorna a quantidade de uns em um array

  lista = [bin(e) for e in range(2**n)]
  lista = sorted(lista,key=conta_uns, reverse=True)
 

  return lista
