from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT)

while True:
    # S
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.6)
    # O
    led.on()
    sleep(0.6)
    led.off()
    sleep(0.6)
    led.on()
    sleep(0.6)
    led.off()
    sleep(0.6)
    led.on()
    sleep(0.6)
    led.off()
    sleep(0.6)