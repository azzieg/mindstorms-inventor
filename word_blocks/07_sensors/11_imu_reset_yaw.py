import hub

# Reset yaw
# Yaw (rotation in the horizontal plane) does not have an absolute 0, so this
# marks the current yaw as 0. Any subsequent yaw values will be relative to it.
hub.motion.yaw_pitch_roll(0)
yield 100 # small delay to avoid some undesired effects, maybe due to averaging
