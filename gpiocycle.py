import RPi.GPIO as GPIO
import time
LISTTT = [16,22,15]
for i in LISTTT:
    PINN =i
    print(i)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PINN,GPIO.OUT)
    print ("LED on")
    GPIO.output(PINN,GPIO.HIGH)
    time.sleep(5)
    print ("LED off")
    GPIO.output(PINN,GPIO.LOW)
    time.sleep(5)
    GPIO.output(PINN,GPIO.HIGH)