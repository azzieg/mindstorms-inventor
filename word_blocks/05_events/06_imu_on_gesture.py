# When gesture
async def stack_function(vm, stack):
    pass # replace this with your event handling program

vm.register_on_gesture(
    "registration_id",
    stack_function,
    2) # 0 is tapped, 2 is shaken, 3 is falling
