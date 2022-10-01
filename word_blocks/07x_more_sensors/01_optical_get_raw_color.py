import math
from util.sensors import get_sensor_value

sensor_value = get_sensor_value(
    "A",
    2, # 2 is for red, 3 is for green, 4 is for blue (mode is actually 5)
    -1, # default value if unknown
    (61,)) # use for Technic color sensor
if sensor_value is None:
    sensor_value = -1
# 0 is no color component or unknown, 255 is maximum color component
return math.floor((sensor_value * 0.249) + 0.5)
