from util.sensors import get_sensor_value

sensor_value = get_sensor_value(
    "A",
    0, # color recognition mode
    -1, # default value if unknown
    (61,)) # use for Technic color sensor
if sensor_value is None:
    sensor_value = -1
# -1 is no color detected, 0 is black, 1 is pink, 3 is blue,
# 4 is azure and teal, 5 is green, 7 is yellow, 9 is red, 10 is white
option = 9
return ((option == sensor_value) or
        # blue, azure and teal are easily confused
        ((option in (3, 4)) and (sensor_value in (3, 4))))
