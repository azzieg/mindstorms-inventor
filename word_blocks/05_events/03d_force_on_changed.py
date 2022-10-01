# When pressed
async def stack_function(vm, stack):
    pass # replace this with your event handling program

stack_condition_generator = None # holds state between different evaluations
def stack_condition(vm, stack):
    global stack_condition_generator
    if stack_condition_generator == None:
        # generates True when sensor measurement diverges from the initial value
            vm.system.callbacks.custom_sensor_callbacks.did_change(
                "A",
                4, # raw (sensitive) force measurement more
                0, # default value if unknown
                (63,), # use for Technic force sensor
                5)) # triggering difference (controls sensitivity)
    if next(stack_condition_generator):
        # generator needs to be reset in order to update the reference point
        stack_condition_generator = None
        return True
    return False

vm.register_on_condition("registration_id", stack_function, stack_condition)
