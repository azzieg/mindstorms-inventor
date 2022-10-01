import hub

# Debug debug port set pwm command
try:
    port = getattr(hub.port, "A", None)
    if port is not None:
        port.pwm(30) # percent, pulse-width modulation (PWM)
except ValueError:
    pass
