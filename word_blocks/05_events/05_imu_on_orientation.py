# When orientation
async def stack_function(vm, stack):
    pass # replace this with your event handling program

vm.register_on_orientation(
    "registration_id",
    stack_function,
    3) # which side facing up triggers the event: 0 is "front", 1 is "top",
       # 2 is "right side", 3 is "back", 4 is "bottom", 5 is "left side"
