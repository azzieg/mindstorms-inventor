from util.movement import from_steering, move_degrees

# Steer distance at speed
await move_degrees(
    vm,
    360, # degrees, 1 rotation = 360 degrees
    from_steering(
        0, # percent, positive is right turn, negative is left; 0 for straight,
           # 100 for clockwise rotation, -100 for counterclockwise rotation
        -50)) # percent, 100 is full speed forward, -50 is half speed backward
