from util.movement import from_steering, move_start

# Start steer at speed
move_start(
    vm,
    from_steering(
        50, # percent, 0 is straight, 100 is rotate, positive for "right"
        75)) # percent, 100 is full speed forward, -50 is half speed backward
