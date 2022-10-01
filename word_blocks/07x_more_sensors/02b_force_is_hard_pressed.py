from util.sensors import get_sensor_value

return get_sensor_value(
    "A",
    0, # force measurement mode, in newtons
    0, # default value if unknown
    (63,) # use for Technic force sensor
) > 5 # force measurement range is from 0 to 10, 5 is half-pressed
