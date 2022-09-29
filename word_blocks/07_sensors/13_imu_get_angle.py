from util.sensors import get_sensor_value

values = get_sensor_value("position", 0, 0, ())
# angles: yaw and roll are from -180 to 179, pitch is from -90 to 90
return values[1] # 0 for yaw (left/right), 1 for pitch (up/down), 2 for roll
