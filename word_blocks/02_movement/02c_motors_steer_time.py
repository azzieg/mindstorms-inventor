from util.movement import from_steering, move_ms

# Steer
await move_ms(
    vm,
    3000, # milliseconds, 1 second = 1000 milliseconds
    from_steering(
        0, # percent, 0 is straight, 100 is rotate, positive for "right"
        vm.store.move_speed()))
