from runtime.extensions import RadioBroadcastExtension

vm.extensions["radiobroadcast"] = RadioBroadcastExtension(rpc, vm) # in setup

# Radiobroadcast broadcast radio signal with value command
await vm.extensions["radiobroadcast"].broadcast(
    3065852031, # CRC32 of the signal name (here: "message")
    "Hello")
