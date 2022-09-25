from util.scratch import pitch_to_freq

# Play sound until done
await vm.system.sound.play_async(
    "/extra_files/Tadaa",
    freq=pitch_to_freq(vm.store.sound_pitch(), 12000, 16000, 20000))
