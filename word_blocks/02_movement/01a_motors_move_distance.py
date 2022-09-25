import math
from util.movement import from_direction, move_degrees
from util.scratch import clamp

# Move
await move_degrees(
    vm,
    math.floor(
        clamp(
            (10 / vm.store.move_calibration()) * 360, # cm to degrees
            -3600000,
            3600000)
        + 0.5), # round to nearest full degree
    from_direction(
        "forward", # or: "back", "counterclockwise", "clockwise"
        vm.store.move_speed()))
