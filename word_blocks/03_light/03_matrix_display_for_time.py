import hub
from util.scratch import convert_image

# Led image for
await vm.system.display.show_async(
    hub.Image(
        convert_image(
            "9909999099000009000909990", # 0 is off, 9 is full brightness
            vm.store.display_brightness())),
     clear=True,
     delay=2000) # milliseconds, 2 seconds = 2000 milliseconds
