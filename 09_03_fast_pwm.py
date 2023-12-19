from machine import Pin, PWM

out_pin = PWM(Pin(16))
out_pin.freq(800)

out_pin.duty_u16(16000) # 50%
