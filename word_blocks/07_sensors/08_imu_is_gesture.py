import hub

def is_shaken():
    return hub.motion.gesture() == 2 # 0 is tapped, 2 is shaken, 3 is falling
