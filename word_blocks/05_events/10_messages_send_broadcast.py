# Event broadcast
vm.broadcast("message")
yield # message might be handled before continuing, but does not have to
