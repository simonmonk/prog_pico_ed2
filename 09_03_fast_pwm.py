from machine import Pin, PWM

out_pin = PWM(Pin(16))
out_pin.freq(1000000)

out_pin.duty_u16(32000) # 50%
