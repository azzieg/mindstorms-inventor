from util.movement import from_steering, move_start

# Start steer
move_start(
    vm,
    from_steering(
        30, # percent, positive is right, negative is left; 0 for straight,
            # 100 for clockwise rotation, -100 for counterclockwise rotation
        vm.store.move_speed()))
