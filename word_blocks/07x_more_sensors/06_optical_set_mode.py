import hub
from util.sensors import _DEFAULT_MODE, is_type

def g_get_device(portName, deviceType):
    return getattr(
        getattr(hub.port, portName, None),
        "device",
        None) if is_type(portName, deviceType) else None

# Color sensor set mode
device = g_get_device("A", 61)
if device:
    # Mode can be a single number, or a list of (mode, component) pairs.
    # For the color sensor it can be 0 for color, 1 for reflectivity,
    # 2 for ambient light and 5 for RGBI. The default is:
    # [(1, 0), (0, 0), (5, 0), (5, 1), (5, 2)]
    # For defaults for other devices, see below.
    device.mode(_DEFAULT_MODE[61]) # device.mode(2) for "ambient"

# Default modes and multi-modes for different devices:
# - motors with absolute positioning: [(1, 0), (2, 2), (3, 1), (0, 0)]
# - motors with relative positioning: [(1, 0), (2, 2), (0, 0)]
# - Technic color sensor: [(1, 0), (0, 0), (5, 0), (5, 1), (5, 2)]
# - Technic distance sensor: [(0, 0)]
# - Technic force sensor: [(0, 0), (1, 0), (4, 0)]
# - Boost color and distance sensor: 8
