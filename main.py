import result_pub
import time
import machine
from machine import Pin
led = Pin(2, Pin.OUT) #Gpio that controls onboard LED
i = 0
while True:
    time.sleep(3)
    led.value(0)
    i += 1
    print("Sending hit:{}".format(i))
    result_pub.sendHit()
    time.sleep(3)
    led.value(1)
