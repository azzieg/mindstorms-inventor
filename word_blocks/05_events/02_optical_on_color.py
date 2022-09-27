import hub
from runtime import VirtualMachine
from util.sensors import get_sensor_value

# When color
async def stack_function(vm, stack):
    pass # replace this with your event handling program

def stack_condition(vm, stack):
    sensor_value = get_sensor_value("A", 0, -1, (61,))
    if sensor_value is None:
        sensor_value = -1
    return 9 == sensor_value # -1 is no color detected, 0 is black, 1 is pink,
                             # 3 is blue, 4 is azure and teal, 5 is green,
                             # 7 is yellow, 9 is red, 10 is white

vm.register_on_condition("registration_id", stack_function, stack_condition)
