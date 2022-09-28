from util.movement import move_ms

# Move distance at speed
await move_ms(
    vm,
    1000, # milliseconds, 1 second = 1000 milliseconds
    (0, 100)) # percent (left, right), left is clockwise for negative values,
              # right is clockwise for positive values
