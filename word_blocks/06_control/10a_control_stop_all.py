# Stop
if hasattr(vm, "reset_devices"):
    vm.reset_devices()
vm.stop_stacks()
while True:
    yield
# this function will never continue
