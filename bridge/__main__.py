from mongo import Mongo
from mqtt import MQTT
import os

mongo = Mongo()
mqtt = MQTT(mongo)

mongo.connect()
mqtt.run()

try:
    os.system('pause')
except KeyboardInterrupt:
    pass

mqtt.stop()
mongo.disconnect()
