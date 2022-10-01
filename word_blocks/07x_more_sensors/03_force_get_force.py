from util.sensors import get_sensor_value

# force in newtons, from 0 (not pressed) to 10 (fully depressed).
return get_sensor_value(
    "A",
    0, # force measurement mode, in newtons
    0, # default value if unknown
    (63,)) # use for Technic force sensor
