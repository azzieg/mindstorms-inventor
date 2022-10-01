from util.sensors import get_sensor_value

sensor_value = get_sensor_value(
    "A",
    0, # long-range distance measurement mode
    200, # default value if unknown
    (62,)) # use for Technic distance sensor
if sensor_value is None:
    sensor_value = 200 # max range is 200 centimeters = 2 meters
return sensor_value < 50 # centimeters
