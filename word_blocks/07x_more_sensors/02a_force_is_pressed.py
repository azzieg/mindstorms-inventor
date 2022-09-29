from util.sensors import get_sensor_value

return get_sensor_value("A", 1, 0, (63,)) == 1 # or: 0 for released
