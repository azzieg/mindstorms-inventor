from util.sensors import get_sensor_value

values = get_sensor_value("position", 0, 0, ())
# angles: yaw and roll are from -180 to 179, pitch is from -90 to 90
return values[1] # 0 is yaw (left/right), 1 is pitch (up/down), 2 is roll
