import RPi.GPIO as GPIO
import time
try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#<-- linha Importante
    GPIO.setup(11, GPIO.OUT)
    while True:
        GPIO.output(11, GPIO.LOW)
        while GPIO.input(7):
            GPIO.output(11, GPIO.HIGH)
        time.sleep(0.1)    
finally:
    GPIO.cleanup()
    print("GPIO.cleanup()")
