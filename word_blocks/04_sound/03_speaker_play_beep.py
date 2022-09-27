# Beep for time
await vm.system.sound.beep_async(
    60, # C is 48, C# is 49, D is 50, Eb is 51, E is 52, F is 53, F# is 54,
        # G is 55, G# is 56, A is 57, Bb is 58, B is 59, add 12 for next octave
    200) # milliseconds, 0.2 seconds = 200 milliseconds
