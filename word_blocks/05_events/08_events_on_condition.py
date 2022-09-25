# When condition
async def stack_function(vm, stack):
    pass # replace this with your event handling program

def stack_condition(vm, stack):
    return False # replace this with your condition returning True to trigger

vm.register_on_condition("registration_id", stack_function, stack_condition)
