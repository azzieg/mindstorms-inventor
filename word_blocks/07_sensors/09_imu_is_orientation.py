import hub

# which side is facing up: 0 is "front", 1 is "top", 2 is "right side",
# 3 is "back", 4 is "bottom", 5 is "left side"
return hub.motion.orientation() == 3
