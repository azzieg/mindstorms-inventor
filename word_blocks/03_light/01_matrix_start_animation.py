import hub
from util.scratch import convert_animation_frame

# Led animation
g_animation = [
    "0000900000000000000000000", # upper right pixel full brightness
    "0000000000000000000050000"] # lower left pixel half brightness
brightness = vm.store.display_brightness()
frames = [
    hub.Image(convert_animation_frame(frame, brightness))
    for frame in g_animation]
vm.system.display.show(
    frames,
    clear=False, # whether to clear or leave the last frame in the end
    delay=125, # milliseconds, 8 frames per second, also for fade effects
    loop=True, # whether to loop the animation
    fade=2) # 1 is "Direct", 2 is "Overlay", 3 is "Slide right",
            # 4 is "Slide left", 5 is "Fade in", 6 is "Fade out"
