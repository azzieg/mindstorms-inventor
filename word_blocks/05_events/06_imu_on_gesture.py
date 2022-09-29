# When gesture
async def stack_function(vm, stack):
    pass # replace this with your event handling program

vm.register_on_gesture(
    "registration_id",
    stack_function,
    2) # 0 for "tapped", 2 for "shaken", 3 for "falling"
