import Adafruit_DHT as dht
import time
sensor = dht.DHT11
pin =21

try:
    while True:
        h,t =dht.read_retry(sensor,pin)
        if h is not None and t is not None:
            print("Temp = {0:0.1f}C Humidity = {1:0.1f}%".format(t,h))          
        else:
            print("Failed to get reading.Try again!")
except KeyboardInterrupt:
    print("Temp by keyboard")
finally:
    print("End of program")