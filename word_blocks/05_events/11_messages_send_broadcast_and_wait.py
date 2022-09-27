# Event broadcastandwait
stacks = vm.broadcast("message")
while any([s.is_active() for s in stacks]): # wait for all listeners to complete
    yield # do something else in the meantime
