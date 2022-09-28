# Motor start speed
(acceleration, deceleration) = vm.store.motor_acceleration("A")
vm.system.motors.on_port("A").run_at_speed(
    75, # percent, positive for clockwise
    stall=vm.store.motor_stall("A"),
    acceleration=acceleration,
    deceleration=deceleration)
