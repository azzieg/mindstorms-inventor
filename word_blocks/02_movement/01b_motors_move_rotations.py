from util.movement import from_direction, move_degrees

# Move
await move_degrees(
    vm,
    360, # degrees, 1 rotation = 360 degrees
    from_direction(
        "counterclockwise", # or: "forward", "back", "clockwise"
        vm.store.move_speed()))
