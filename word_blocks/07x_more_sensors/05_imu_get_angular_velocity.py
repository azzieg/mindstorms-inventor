from util.sensors import get_sensor_value

values = get_sensor_value("gyroscope", 0, (0, 0, 0), ())
return values[2] # 0 for "x", 1 for "y", 2 for "z"
