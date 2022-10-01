from util.sensors import get_sensor_value

return get_sensor_value(
    "A",
    2, # relative position measurement mode, in degrees
    0, # default value if unknown
    (49, 48, 65, 76, 75, 46, 47, 38)) # use for motors with positioning
