from util.sensors import get_sensor_value

position = get_sensor_value(
    "A",
    3, # absolute position measurement mode, in degrees
    0, # default value if unknown
    (49, 48, 65, 76, 75, 46, 47)) # use for motors with absolute positioning
if position < 0:
    position = position + 360
return position
