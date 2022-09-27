from util.scratch import to_number
from util.sensors import get_sensor_value

# which side facing up: None is unavailable, 0 is "front", 1 is "top",
# 2 is "right side", 3 is "back", 4 is "bottom", 5 is "left side"
return to_number(get_sensor_value("orientation", 1, None, ()))
