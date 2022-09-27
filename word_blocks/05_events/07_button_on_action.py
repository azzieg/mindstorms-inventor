# When button
async def stack_function(vm, stack):
    pass # replace this with your event handling program

vm.register_on_button(
    "stack_id",
    stack_function,
    "left", # or: "right"
    "released") # or: "pressed"
