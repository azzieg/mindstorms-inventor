from util.sensors import get_sensor_value

values = get_sensor_value("accelerometer", 0, (0, 0, 0), ())
# measured g-force projected onto x, y and z axes, 1000 = 1g (approximately)
return values[1] # 0 for "x", 1 for "y", 2 for "z"
