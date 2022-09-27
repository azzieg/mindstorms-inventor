# Beep
vm.system.sound.beep(
    60, # C is 48, C# is 49, D is 50, Eb is 51, E is 52, F is 53, F# is 54,
        # G is 55, G# is 56, A is 57, Bb is 58, B is 59, add 12 for next octave
    32767) # plays the beep as long as possible (approximately 33 seconds)
yield 10 # a small delay, most likely to avoid some undesired effects
