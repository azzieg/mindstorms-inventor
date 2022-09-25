from util.sensors import get_sensor_value

# When pressed
async def stack_function(vm, stack):
    pass # replace this with your event handling program

def stack_condition(vm, stack):
    return get_sensor_value("A", 0, 0, (63,)) > 5

vm.register_on_condition("registration_id", stack_function, stack_condition)
