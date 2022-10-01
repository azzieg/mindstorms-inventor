# When pressed
async def stack_function(vm, stack):
    pass # replace this with your event handling program

stack_condition_generator = None # holds state between different evaluations
def stack_condition(vm, stack):
    global stack_condition_generator
    if stack_condition_generator == None:
        # generates True on sensor measurement falling below the threshold
        # (if the initial value is already below then in must reach it first)
        stack_condition_generator = (
            vm.system.callbacks.custom_sensor_callbacks.is_less_than(
                "A",
                1, # detect button presses mode
                0, # default value if unknown
                (63,), # use for Technic force sensor
                1)) # 0 is depressed, 1 is pressed
    if next(stack_condition_generator):
        # this generator reset is probably unnecessary
        stack_condition_generator = None
        return True
    return False

vm.register_on_condition("registration_id", stack_function, stack_condition)
