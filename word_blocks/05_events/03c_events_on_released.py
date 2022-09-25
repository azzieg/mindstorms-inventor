# When pressed
async def stack_function(vm, stack):
    pass # replace this with your event handling program

stack_condition_generator = None # holds state between different evaluations
def stack_condition(vm, stack):
    global stack_condition_generator
    if stack_condition_generator == None:
        stack_condition_generator = (
            vm.system.callbacks.custom_sensor_callbacks.is_less_than(
                "A", 1, 0, (63,), 1))
    if next(stack_condition_generator):
        stack_condition_generator = None
        return True
    return False

vm.register_on_condition("registration_id", stack_function, stack_condition)
