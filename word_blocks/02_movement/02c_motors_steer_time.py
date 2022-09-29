from util.movement import from_steering, move_ms

# Steer
await move_ms(
    vm,
    3000, # milliseconds, 1 second = 1000 milliseconds
    from_steering(
        0, # percent, positive is right turn, negative is left; 0 for straight,
           # 100 for clockwise rotation, -100 for counterclockwise rotation
        vm.store.move_speed()))
