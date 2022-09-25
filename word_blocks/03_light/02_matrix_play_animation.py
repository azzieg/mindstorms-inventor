import hub
from util.scratch import convert_animation_frame

# Led animation until done
g_animation = ["9909999099000009000909990"] # 0 is off, 9 is full brightness
brightness = vm.store.display_brightness()
frames = [
    hub.Image(convert_animation_frame(frame, brightness))
    for frame in g_animation]
await vm.system.display.show_async(
    frames,
    clear=False, # whether to clear or leave the last frame in the end
    delay=250, # milliseconds, 4 frames per second, also for fade effects
    loop=False, # whether to loop the animation (will never finish if true)
    fade=5) # 1 is "Direct", 2 is "Overlay", 3 is "Slide right",
            # 4 is "Slide left", 5 is "Fade in", 6 is "Fade out"
