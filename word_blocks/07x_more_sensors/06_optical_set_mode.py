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
    device.mode(_DEFAULT_MODE[61]) # or: device.mode(2) for "ambient"
