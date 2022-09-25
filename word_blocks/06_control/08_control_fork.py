# Fork
done = False
async def fork():
    pass # replace with your code to be run in parallel
    nonlocal done
    done = True
stack.fork("fork", fork())
pass # replace with your code doing the other thing in parallel
while not done:
    yield
# at this point both operations will be complete
