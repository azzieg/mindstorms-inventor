from util.scratch import compare

# When timer
async def stack_function(vm, stack):
    pass # replace this with your event handling program

def stack_condition(vm, stack):
    return compare(vm.get_time() / 1000, 1) > 0 # 1000 milliseconds = 1 second

vm.register_on_condition("registration_id", stack_function, stack_condition)
