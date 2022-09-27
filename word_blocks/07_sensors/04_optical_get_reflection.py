from util.sensors import get_sensor_value

def get_reflection():
    return get_sensor_value("A", 1, -1, (61,)) # percent
