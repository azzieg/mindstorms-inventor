from util.sensors import get_sensor_value

def get_distance():
    sensor_value = get_sensor_value("A", 0, 200, (62,))
    if sensor_value is None:
        sensor_value = 200 # max range is 200 centimeters = 2 meters
    return sensor_value # centimeters
