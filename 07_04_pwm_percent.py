from machine import Pin, PWM
from utime import sleep

led = PWM(Pin('LED'))
led.freq(1000)

while True:
    brightness_str = input('brightness (0-100):')
    brightness = int(int(brightness_str) * 65534 / 100)
    led.duty_u16(brightness)