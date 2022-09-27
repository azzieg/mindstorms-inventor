import hub
from util.scratch import to_number

gesture = hub.motion.gesture()
# None is no gesture detected, 0 is "tapped", 2 is "shaken", 3 is "falling"
return to_number(gesture if (gesture is not None) else -1)
