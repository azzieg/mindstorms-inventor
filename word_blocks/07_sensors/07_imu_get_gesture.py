import hub

gesture = hub.motion.gesture()
# None/-1 when no gesture detected, 0 is "tapped", 2 is "shaken", 3 is "falling"
return gesture if (gesture is not None) else -1
