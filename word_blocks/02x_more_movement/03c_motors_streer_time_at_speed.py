from util.movement import from_steering, move_ms

# Steer distance at speed
await move_ms(
    vm,
    2000, # milliseconds, 1 second = 1000 milliseconds
    from_steering(
        -100, # percent, 0 is straight, 100 is rotate, negative for "left"
        25)) # percent, 100 is full speed forward, -50 is half speed backward
