from util.movement import from_steering, move_degrees

# Steer
await move_degrees(
    vm,
    360, # degrees, 1 rotation = 360 degrees
    from_steering(
        -60, # percent, 0 is straight, 100 is rotate, negative for "left"
        vm.store.move_speed()))
