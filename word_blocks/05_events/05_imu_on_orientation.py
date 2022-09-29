# When orientation
async def stack_function(vm, stack):
    pass # replace this with your event handling program

vm.register_on_orientation(
    "registration_id",
    stack_function,
    3) # which side facing up triggers the event: 0 for "front", 1 for "top",
       # 2 for "right side", 3 for "back", 4 for "bottom", 5 for "left side"
