from runtime.extensions import RadioBroadcastExtension

# Radiobroadcast when ireceive radio signal hat
async def stack_function(vm, stack):
    pass # replace this with your event handling program

vm.extensions["radiobroadcast"] = RadioBroadcastExtension(rpc, vm) # in setup
vm.extensions["radiobroadcast"].register(
    3065852031, # CRC32 of the signal name (here: "message")
    stack_function,
    "registration_id")
