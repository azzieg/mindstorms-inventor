import math
from util.scratch import clamp

# Sound changeeffectby
vm.store.sound_pitch(
    math.floor(
        # min is -360 (low), max is 360 (high)
        clamp(vm.store.sound_pitch() + 10, -360, 360)
        + 0.5)) # round to the nearest integer
