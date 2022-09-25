# Motor start direction
(acceleration, deceleration) = vm.store.motor_acceleration("A")
vm.system.motors.on_port("A").run_at_speed(
    -vm.store.motor_speed("A"), # negative for counterclockwise
    stall=vm.store.motor_stall("A"),
    acceleration=acceleration,
    deceleration=deceleration)
