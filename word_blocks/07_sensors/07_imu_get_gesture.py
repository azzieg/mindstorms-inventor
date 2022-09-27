import hub

def get_gesture():
    return hub.motion.gesture() # 0 is tapped, 2 is shaken, 3 is falling
