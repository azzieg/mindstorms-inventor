import hub

# Center button light
color = 9
if color in [4, 5]: # remaps azure to teal and teal to green for some reason
    color = color + 1
# 0 is off/black, 1 is pink, 2 is purple/violet, 3 is blue, 4 is azure,
# 5 is teal/cyan, 6 is green, 7 is yellow, 8 is orange, 9 is red, 10 is white
hub.led(color)
