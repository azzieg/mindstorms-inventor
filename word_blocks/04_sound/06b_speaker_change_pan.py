import math
from util.scratch import clamp

# Sound changeeffectby
vm.store.sound_pan(
    math.floor(
        # min is -100 (left), max is 100 (right)
        clamp(vm.store.sound_pan() - 10, -100, 100)
        + 0.5)) # round to the nearest integer
