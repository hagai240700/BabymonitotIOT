import Adafruit_DHT as dht
from config import DHT_PIN

def read_temp_humidity():
    h, t = dht.read_retry(dht.AM2302, DHT_PIN)
    return h, t