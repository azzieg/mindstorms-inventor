# Motor turn for speed
(acceleration, deceleration) = vm.store.motor_acceleration("A")
vm.store.motor_last_status(
    "A",
    await vm.system.motors.on_port("A").run_for_time_async(
        1000, # milliseconds, 1 second = 1000 milliseconds
        75, # percent, positive for clockwise
        stall=vm.store.motor_stall("A"),
        stop=vm.store.motor_stop("A"),
        acceleration=acceleration,
        deceleration=deceleration))
