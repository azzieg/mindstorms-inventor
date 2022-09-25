# Stop other stacks
if hasattr(vm, "reset_devices"):
    vm.reset_devices()
vm.stop_stacks(except_stack=stack)
# this function will continue
