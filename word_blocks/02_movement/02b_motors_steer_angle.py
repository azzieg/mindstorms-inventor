from util.movement import from_steering, move_degrees

# Steer
await move_degrees(
    vm,
    360, # wheel rotation in degrees, 1 rotation = 360 degrees
    from_steering(
        -60, # percent, positive is right, negative is left; 0 for straight,
             # 100 for clockwise rotation, -100 for counterclockwise rotation
        vm.store.move_speed()))
