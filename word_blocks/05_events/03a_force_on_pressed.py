from util.sensors import get_sensor_value

# When pressed
async def stack_function(vm, stack):
    pass # replace this with your event handling program

def stack_condition(vm, stack):
    return get_sensor_value(
        "A",
        1, # detect button presses mode
        0, # default value if unknown
        (63,) # use for Technic force sensor
    ) == 1 # 0 is depressed, 1 is pressed

vm.register_on_condition("registration_id", stack_function, stack_condition)
