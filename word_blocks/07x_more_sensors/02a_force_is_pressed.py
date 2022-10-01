from util.sensors import get_sensor_value

return get_sensor_value(
    "A",
    1, # detect button presses mode
    0, # default value if unknown
    (63,) # use for Technic force sensor
) == 1 # or: 0 for released
