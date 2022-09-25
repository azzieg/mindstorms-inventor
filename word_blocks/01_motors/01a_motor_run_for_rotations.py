# Motor turn for direction
(acceleration, deceleration) = vm.store.motor_acceleration("A")
vm.store.motor_last_status(
    "A",
    await vm.system.motors.on_port("A").run_for_degrees_async(
        360, # degrees, 1 rotation = 360 degrees
        -vm.store.motor_speed("A"), # negative for counterclockwise
        stall=vm.store.motor_stall("A"),
        stop=vm.store.motor_stop("A"),
        acceleration=acceleration,
        deceleration=deceleration))
