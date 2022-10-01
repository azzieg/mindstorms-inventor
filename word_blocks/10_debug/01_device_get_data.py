import hub

result = ""
port = getattr(hub.port, "A", None)
if getattr(port, "device", None) is not None:
    try:
        modes = port.device.mode()
        # 0 for RAW (raw value), 1 for PCT (percent), 2 for SI (standard unit)
        results = port.device.get(0)
        index = modes.index((1, 2)) # (M, Ds) for mode and data component
        result = results[index]
    except ValueError:
        pass
return result
