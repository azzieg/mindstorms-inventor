from util.sensors import get_sensor_value

values = get_sensor_value("position", 0, 0, ())
return values[1] # 0 is yaw (left/right), 1 is pitch (up/down), 2 is roll
