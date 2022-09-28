import math
from util.movement import move_degrees
from util.scratch import clamp

# Move distance at speed
await move_degrees(
    vm,
    math.floor(
        clamp(
            (10 / vm.store.move_calibration()) * 360, # cm to degrees
            -3600000,
            3600000)
        + 0.5), # round to nearest full degree
    (25, 75)) # percent (left, right), left is clockwise for negative values,
              # right is clockwise for positive values
