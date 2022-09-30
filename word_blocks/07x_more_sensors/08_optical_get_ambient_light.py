import hub
from util.sensors import is_type

def g_get_device(portName, deviceType):
    return getattr(
        getattr(hub.port, portName, None),
        "device",
        None) if is_type(portName, deviceType) else None

device = g_get_device("A", 61)
return device.get()[0] if device else 0 # percent
