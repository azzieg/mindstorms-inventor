from util.movement import from_steering

# Start steer at power
vm.system.move.on_pair(*vm.store.move_pair()).start_at_powers(
    *from_steering(
        -30, # percent, 0 is straight, 100 is rotate, positive for "right"
        50, # percent, 100 is full power forward, -50 is half power backward
        True))
