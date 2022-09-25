import math
from util.scratch import clamp

# Sound changeeffectby
vm.store.sound_pitch( # or: sound_pan
    math.floor(
        clamp(vm.store.sound_pitch() + 10, -360, 360) # or: -100 to 100 for pan
        + 0.5)) # round to the nearest integer
