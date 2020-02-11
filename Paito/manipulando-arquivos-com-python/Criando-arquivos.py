arquivo = open('numeros.txt','w')
for linha in range(1,101):
  arquivo.write('{linha}\n'.format(linha=linha))
arquivo.close()
