#créditos para meu grupo da aula de Hardware
#Algoritimo que controla as portas paralelas para acender leds

import parallel #importa a biblioteca, parallel, que ira controlar as saidas digitais
import time #esse modulo, time, sera usado para a funcao "pisca" 
 
p = parallel.Parallel() # Parallel() é uma classe 

leds=[0,1,2,4,8,16,32,64,128,255] # um lista com valores na base 10, sera usada pela funcao, setData(x)
                                  # onde valor x é um dos itens da lista "leds"

#----------------------------------------------------------------------------------------------------------

def piscar():
  led = input('(1-8)leds; (9)todos :')
  print('(ctrl+c) para parar de piscar')
  while True:
    try:
      p.setData(leds[led])
      time.sleep(0.3)
      p.setData(leds[0])
      time.sleep(0.3)

    except: # quando voce aperta ctrl+c, o cogigo entra nesse execept
      p.setData(0)
      return

#-------------------------------------------------------------------------------------------------------------

try:
  while True:
    led=int(input('(1-8)leds; (9)todos; (0)off; (10)piscar :'))
    if led == 10:
      piscar()
    else:
      p.setData(leds[led] ) # essa linha liga o(s) led(s)

finally: # quando voce sai do codigo
  p.setData(0) # todas as saidas sao dadas como Falso

