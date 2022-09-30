from runtime.extensions import RadioBroadcastExtension

vm.extensions["radiobroadcast"] = RadioBroadcastExtension(rpc, vm) # in setup

return vm.extensions["radiobroadcast"].value( # returns 0 for no message
    3065852031) # CRC32 of the signal name (here: "message")
