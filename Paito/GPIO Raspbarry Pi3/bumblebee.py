import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

#motor A
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)

#motor B
gpio.setup(29, gpio.OUT)
gpio.setup(31, gpio.OUT)
print("init.Bumblebee")
try:
    while True:
        user_input=input("valor: ")
        if user_input == "1":
            gpio.output(11, gpio.LOW)
            gpio.output(13, gpio.LOW)
            gpio.output(29, gpio.LOW)
            gpio.output(31, gpio.LOW)
            
        elif user_input == "w":
            gpio.output(11, gpio.HIGH)
            gpio.output(13, gpio.LOW)
            gpio.output(29, gpio.HIGH)
            gpio.output(31, gpio.LOW)
            
        elif user_input == "s":
            gpio.output(11, gpio.LOW)
            gpio.output(13, gpio.HIGH)
            gpio.output(29, gpio.LOW)
            gpio.output(31, gpio.HIGH)
            
        elif user_input == "a":
            gpio.output(11, gpio.HIGH)
            gpio.output(13, gpio.LOW)
            gpio.output(29, gpio.LOW)
            gpio.output(31, gpio.HIGH)
            time.sleep(0.1)
            gpio.output(11, gpio.LOW)
            gpio.output(13, gpio.LOW)
            gpio.output(29, gpio.LOW)
            gpio.output(31, gpio.LOW)
            
        elif user_input == "d":
            gpio.output(11, gpio.LOW)
            gpio.output(13, gpio.HIGH)
            gpio.output(29, gpio.HIGH)
            gpio.output(31, gpio.LOW)
            time.sleep(0.1)
            gpio.output(11, gpio.LOW)
            gpio.output(13, gpio.LOW)
            gpio.output(29, gpio.LOW)
            gpio.output(31, gpio.LOW)
finally:
    gpio.output(11, gpio.LOW)
    gpio.output(13, gpio.LOW)
    gpio.output(29, gpio.LOW)
    gpio.output(31, gpio.LOW)
    gpio.cleanup()
    print("gpio.cleanup()")
