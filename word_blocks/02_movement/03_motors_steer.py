from util.movement import from_steering, move_start

# Start steer
move_start(
    vm,
    from_steering(
        30, # percent, 0 is straight, 100 is rotate, positive for "right"
        vm.store.move_speed()))
