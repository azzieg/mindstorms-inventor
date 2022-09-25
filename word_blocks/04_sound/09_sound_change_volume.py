# Sound changevolumeby
new_volume = math.floor(
    clamp(vm.system.sound.get_volume() + -10, 0, 100) # percent, min 0, max 100
    + 0.5) # round to the nearest integer
vm.system.sound.set_volume(new_volume)
vm.store.sound_volume(new_volume)
