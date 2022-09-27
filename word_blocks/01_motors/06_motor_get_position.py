from util.sensors import get_sensor_value

def get_position():
    position = get_sensor_value("A", 3, 0, (49, 48, 65, 76, 75, 46, 47))
    if position < 0:
        position = position + 360
    return position # degrees
