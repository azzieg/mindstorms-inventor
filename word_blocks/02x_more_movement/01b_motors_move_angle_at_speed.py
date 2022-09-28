from util.movement import move_degrees

# Move distance at speed
await move_degrees(
    vm,
    360, # degrees, 1 rotation = 360 degrees
    (-50, 50)) # percent (left, right), left is clockwise for negative values,
               # right is clockwise for positive values
