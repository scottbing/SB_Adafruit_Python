import Adafruit_DHT
from Adafruit_IO import RequestError, Client, Feed

ADAFRUIT_IO_KEY = 'aio_RISP150nOSJ2qB35Z51uhYOQw9DO'
ADAFRUIT_IO_USERNAME = 'piberrypi'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))

    if humidity is not None and temperature is not None:
        try: # if we have a 'temperature' feed
            digital = aio.feeds('temperature')
        except RequestError: # create a tmperature feed
            feed = Feed(name="temperature")
            digital = aio.create_feed(feed)
        
    else:
        print("Failed to retrieve data from humidity sensor")
