import time
import RPi.GPIO
try:
    RPi.GPIO.setmode(RPi.GPIO.BOARD)
    RPi.GPIO.setup(11, RPi.GPIO.OUT)
    for c in range(99999):
        RPi.GPIO.output(11, RPi.GPIO.HIGH)
        time.sleep(0.1)
        RPi.GPIO.output(11, RPi.GPIO.LOW)
        time.sleep(0.1)
finally:
    RPi.GPIO.cleanup()
