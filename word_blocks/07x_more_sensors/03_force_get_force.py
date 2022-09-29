from util.sensors import get_sensor_value

# force in newtons, from 0 (not pressed) to 10 (fully depressed).
return get_sensor_value("A", 0, 0, (63,))
