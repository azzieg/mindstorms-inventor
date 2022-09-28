from util.constants import INTERRUPTED

# 0 means completed (or stopped), 1 means interrupted (overridden),
# 2 means stalled (physically blocked)
return vm.store.move_last_status() == INTERRUPTED
