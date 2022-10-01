import hub

# Debug debug port set mode command
try:
    port = getattr(hub.port, "A", None)
    if getattr(port, "device", None) is not None:
        port.device.mode(1) # M (mode)
except ValueError:
    pass
