from util.sensors import get_sensor_value

return get_sensor_value(
    "A",
    1, # reflectance measurement mode, in percent
    -1, # default value if unknown
    (61,) # use for Technic color sensor
) > 75
