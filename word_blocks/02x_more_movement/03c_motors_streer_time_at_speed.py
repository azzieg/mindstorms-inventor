from util.movement import from_steering, move_ms

# Steer distance at speed
await move_ms(
    vm,
    2000, # milliseconds, 1 second = 1000 milliseconds
    from_steering(
        -100, # percent, positive is right, negative is left; 0 for straight,
              # 100 for clockwise rotation, -100 for counterclockwise rotation
        25)) # percent, 100 is full speed forward, -50 is half speed backward
