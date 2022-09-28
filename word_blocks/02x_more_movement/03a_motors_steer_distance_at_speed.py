import math
from util.movement import from_steering, move_degrees
from util.scratch import clamp

# Steer distance at speed
await move_degrees(
    vm,
    math.floor(
        clamp(
            (20 / vm.store.move_calibration()) * 360, # cm to degrees
            -3600000,
            3600000)
        + 0.5),
    from_steering(
        -50, # percent, 0 is straight, 100 is rotate, negative for "left"
        75)) # percent, 100 is full speed forward, -50 is half speed backward
