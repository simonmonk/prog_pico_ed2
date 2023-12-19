from microdot import Microdot
from machine import ADC
import mm_wlan

ssid = 'Monk'
password = 'd4daaa7eda'

temp_sensor = ADC(4)
points_per_volt = 3.3 / 65535

app = Microdot()  
mm_wlan.connect_to_network(ssid, password)

def read_temp_c():
    reading = temp_sensor.read_u16() * points_per_volt
    temp_c = 27 - (reading - 0.706)/0.001721
    return temp_c

@app.route('/')
def index(request):
    return 'Temperature: ' + str(read_temp_c())

app.run(port=80)
