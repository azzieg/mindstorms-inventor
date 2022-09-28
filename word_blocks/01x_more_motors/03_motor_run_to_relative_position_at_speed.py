# Motor go to relative position
(acceleration, deceleration) = vm.store.motor_acceleration("A")
vm.store.motor_last_status(
    "A",
    await vm.system.motors.on_port("A").run_to_relative_position_async(
        180, # degrees
        75, # percent, positive for clockwise
        stall=vm.store.motor_stall("A"),
        stop=vm.store.motor_stop("A"),
        acceleration=acceleration,
        deceleration=deceleration))
