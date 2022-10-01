import hub
import math
from util.scratch import clamp, to_number

# Debug debug port mode set data command
try:
    port = getattr(hub.port, "A", None)
    if getattr(port, "device", None) is not None:
        port.device.mode(
            1, # M (mode)
            # the following simply produces bytes([2, 3])
            bytes(
                "".join([
                    chr(math.floor(clamp(to_number(p), 0, 255) + 0.5))
                    for p in "2 3".split()]),
                "utf-8"))
except ValueError:
    pass
