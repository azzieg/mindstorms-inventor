from util.movement import from_direction, move_ms

# Move
await move_ms(
    vm,
    1000, # milliseconds, 1 second = 1000 milliseconds
    from_direction(
        "back", # or: "forward", "counterclockwise", "clockwise"
        vm.store.move_speed()))
