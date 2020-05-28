import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT) #GREEN
GPIO.setup(20, GPIO.OUT) #RED

try:
    while(True):
        GPIO.output(20,True)
        GPIO.output(21,False)
        time.sleep(1)
        GPIO.output(20,False)
        GPIO.output(21,True)
        time.sleep(1)

except expression as e:
        print(e)    

finally:
    GPIO.cleanup()