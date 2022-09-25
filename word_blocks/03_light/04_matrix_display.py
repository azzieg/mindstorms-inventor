import hub
from util.scratch import convert_image

# Led image
vm.system.display.show(
    hub.Image(
        convert_image(
            "9909999099000009000909990", # 0 is off, 9 is full brightness
            vm.store.display_brightness())),
    clear=False)
