# Motor start power
vm.system.motors.on_port("A").pwm(
    75, # percent, positive for clockwise
    stall=vm.store.motor_stall("A"))
