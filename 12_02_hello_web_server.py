from microdot import Microdot
import mm_wlan

ssid = 'Network'
password = 'password'

app = Microdot()  
mm_wlan.connect_to_network(ssid, password)

@app.route('/')
def index(request):
    return 'Hello from Pico W'

app.run(port=80)