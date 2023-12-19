from machine import Pin, I2C
import mm_wlan
import urequests
import json
from utime import sleep
from ssd1306 import SSD1306_I2C

ssid = 'Network'
password = 'WiFi password'
key = 'ea751fc7712f2705=e8a448213b712'
location = 'lat=53.925854&lon=-3.021994'
api_base = 'http://api.openweathermap.org/data/2.5/weather?'
url = api_base + location + '&appid=' + key
update_period = 60 # seconds


i2c = I2C(0, sda=Pin(4, pull=Pin.PULL_UP), scl=Pin(5, pull=Pin.PULL_UP))
oled = SSD1306_I2C(128, 32, i2c)

def get_weather():
    if not mm_wlan.is_connected():
        mm_wlan.connect_to_network(ssid, password)
    response = urequests.get(url)
    if (response.status_code == 200):
        data = json.loads(response.text)
        description = data['weather'][0]['description']
#     print(data)
        temp = data['main']['temp'] - 273.15
        return (temp, description)
    else:
        return(0, 'unavailable')
        
def update_display():
    temp, description = get_weather()
    oled.fill(0)
    temp_str = '{:.1f} deg C'.format(temp)
    oled.text(temp_str, 0, 0, 1)
    oled.text(description, 0, 20, 1)
    oled.show()

