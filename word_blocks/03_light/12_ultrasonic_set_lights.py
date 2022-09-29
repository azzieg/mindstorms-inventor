import hub
import math
from util.scratch import clamp, percent_to_int, to_number
from util.sensors import is_type

# Ultrasonic light up
port = getattr(hub.port, "A", None)
if getattr(port, "device", None) and is_type("A", 62): # for ultrasonic sensor
    # This could be simplified by operating on lists rather than strings.
    data = "".join([
        chr(percent_to_int(math.floor(clamp(to_number(p), 0, 100) + 0.5), 87))
        for p in "100 100 0 0".split()]) # "UL UR LL LR" brightness percentage
    # If your data is simply a list then remove the encoding parameter.
    port.device.mode(5, bytes(data, "utf-8"))
