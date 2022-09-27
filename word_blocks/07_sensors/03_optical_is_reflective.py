from util.sensors import get_sensor_value

def is_reflective():
    return get_sensor_value("A", 1, -1, (61,)) > 75 # percent
