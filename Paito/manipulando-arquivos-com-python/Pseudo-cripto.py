with open('mensagem.txt') as file:
  nova_txt = []
  txt = file.read()
  
  for word in txt.replace('\n', '-').split('-')[:-1]:
    nova_word = ''
    for w in word:
      if w in 'aeiou':nova_word += '*' 
      else: nova_word += w
    nova_txt.append(nova_word)
    
  with open('cripto.txt', 'w') as c:
    for k in nova_txt:
      c.write(k+'\n')
      
