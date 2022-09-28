# Start dual power
vm.system.move.on_pair(*vm.store.move_pair()).start_at_powers(
    -75, # left percent, clockwise for negative values
    25) # right percent, clockwise for positive values
