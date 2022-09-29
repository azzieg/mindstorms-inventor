from util.movement import from_steering, move_start

# Start steer at speed
move_start(
    vm,
    from_steering(
        50, # percent, positive is right turn, negative is left; 0 for straight,
            # 100 for clockwise rotation, -100 for counterclockwise rotation
        75)) # percent, 100 is full speed forward, -50 is half speed backward
