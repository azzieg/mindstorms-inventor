import math
from util.movement import from_steering, move_degrees
from util.scratch import clamp

# Steer
await move_degrees(
    vm,
    math.floor(
        clamp(
            (20 / vm.store.move_calibration()) * 360, # cm to degrees
            -3600000,
            3600000)
        + 0.5), # round to nearest full degree
    from_steering(
        30, # percent, positive is right turn, negative is left; 0 for straight,
            # 100 for clockwise rotation, -100 for counterclockwise rotation
        vm.store.move_speed()))
