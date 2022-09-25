# Control wait until
while True:
    # It might be simpler to negate the condition and use it above instead.
    if False: # replace this with your condition returning True to continue
        break
    yield 0 # do something else in the meantime
