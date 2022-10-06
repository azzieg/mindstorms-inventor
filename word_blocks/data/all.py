import hub
import math
import urandom
import util.sensors
from runtime import Stack, VirtualMachine
from runtime.extensions import RadioBroadcastExtension, SoundExtension
from system.display import rotate_orientation, set_current_orientation_from_ui_value
from util.constants import INTERRUPTED, NUMBER, STRING
from util.movement import from_direction, from_steering, move_degrees, move_ms, move_start, move_stop
from util.scratch import clamp, compare, convert_animation_frame, convert_brightness, convert_image, get_variable, percent_to_int, pitch_to_freq, to_boolean, to_number
from util.sensors import _DEFAULT_MODE, get_sensor_value, is_type

g_animation = ["0000900000000000000000000", "0000000000000000000050000"]
g_animation_1 = ["9909999099000009000909990"]
def g_get_device(portName, deviceType):
    return getattr(getattr(hub.port, portName, None), "device", None) if is_type(portName, deviceType) else None


# When program starts
async def stack_1(vm, stack):
    # Motor turn for direction
    (acceleration, deceleration) = vm.store.motor_acceleration("A")
    vm.store.motor_last_status("A", await vm.system.motors.on_port("A").run_for_degrees_async(360, -vm.store.motor_speed("A"), stall=vm.store.motor_stall("A"), stop=vm.store.motor_stop("A"), acceleration=acceleration, deceleration=deceleration))
    # Motor turn for direction
    (acceleration_1, deceleration_1) = vm.store.motor_acceleration("A")
    vm.store.motor_last_status("A", await vm.system.motors.on_port("A").run_for_time_async(1000, vm.store.motor_speed("A"), stall=vm.store.motor_stall("A"), stop=vm.store.motor_stop("A"), acceleration=acceleration_1, deceleration=deceleration_1))
    # Motor go direction to position
    (acceleration_2, deceleration_2) = vm.store.motor_acceleration("A")
    vm.store.motor_last_status("A", await vm.system.motors.on_port("A").run_to_position_async(180, abs(vm.store.motor_speed("A")), "shortest", stall=vm.store.motor_stall("A"), stop=vm.store.motor_stop("A"), acceleration=acceleration_2, deceleration=deceleration_2))
    # Motor start direction
    (acceleration_3, deceleration_3) = vm.store.motor_acceleration("A")
    vm.system.motors.on_port("A").run_at_speed(-vm.store.motor_speed("A"), stall=vm.store.motor_stall("A"), acceleration=acceleration_3, deceleration=deceleration_3)
    # Motor stop
    vm.system.motors.on_port("A").stop(vm.store.motor_stop("A"))
    # Motor set speed
    vm.store.motor_speed("A", 75)
    # Data setvariableto
    position = get_sensor_value("A", 3, 0, (49, 48, 65, 76, 75, 46, 47))
    if position < 0:
        position = position + 360
    vm.vars["Var"] = (NUMBER, position)
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, get_sensor_value("A", 1, 0, (49, 48, 65, 76, 75, 46, 47, 38)))
    # Motor turn for speed
    (acceleration_4, deceleration_4) = vm.store.motor_acceleration("A")
    vm.store.motor_last_status("A", await vm.system.motors.on_port("A").run_for_degrees_async(360, 75, stall=vm.store.motor_stall("A"), stop=vm.store.motor_stop("A"), acceleration=acceleration_4, deceleration=deceleration_4))
    # Motor turn for speed
    (acceleration_5, deceleration_5) = vm.store.motor_acceleration("A")
    vm.store.motor_last_status("A", await vm.system.motors.on_port("A").run_for_time_async(1000, 75, stall=vm.store.motor_stall("A"), stop=vm.store.motor_stop("A"), acceleration=acceleration_5, deceleration=deceleration_5))
    # Motor start speed
    (acceleration_6, deceleration_6) = vm.store.motor_acceleration("A")
    vm.system.motors.on_port("A").run_at_speed(75, stall=vm.store.motor_stall("A"), acceleration=acceleration_6, deceleration=deceleration_6)
    # Motor go to relative position
    (acceleration_7, deceleration_7) = vm.store.motor_acceleration("A")
    vm.store.motor_last_status("A", await vm.system.motors.on_port("A").run_to_relative_position_async(180, 75, stall=vm.store.motor_stall("A"), stop=vm.store.motor_stop("A"), acceleration=acceleration_7, deceleration=deceleration_7))
    # Motor set degree counted
    vm.system.motors.on_port("A").preset(90)
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, get_sensor_value("A", 2, 0, (49, 48, 65, 76, 75, 46, 47, 38)))
    # Motor start power
    vm.system.motors.on_port("A").pwm(75, stall=vm.store.motor_stall("A"))
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, get_sensor_value("A", 0, 0, (49, 48, 65, 76, 75, 46, 47, 38)))
    # Motor set stop method
    vm.store.motor_stop("A", 1)
    # Motor set acceleration
    vm.store.motor_acceleration("A", (350, 350))
    # Motor set stall detection
    vm.store.motor_stall("A", True)
    # Control wait until
    while True:
        if vm.store.motor_last_status("A") == INTERRUPTED:
            break
        yield 0

# When program starts
async def stack_2(vm, stack):
    # Move
    await move_degrees(vm, math.floor(clamp((10 / vm.store.move_calibration()) * 360, -3600000, 3600000) + 0.5), from_direction("forward", vm.store.move_speed()))
    # Move
    await move_degrees(vm, 360, from_direction("counterclockwise", vm.store.move_speed()))
    # Move
    await move_ms(vm, 1000, from_direction("back", vm.store.move_speed()))
    # Steer
    await move_degrees(vm, math.floor(clamp((20 / vm.store.move_calibration()) * 360, -3600000, 3600000) + 0.5), from_steering(30, vm.store.move_speed()))
    # Steer
    await move_degrees(vm, 360, from_steering(-60, vm.store.move_speed()))
    # Steer
    await move_ms(vm, 3000, from_steering(0, vm.store.move_speed()))
    # Start steer
    move_start(vm, from_steering(30, vm.store.move_speed()))
    # Stop move
    move_stop(vm)
    # Movement speed
    vm.store.move_speed(50)
    # Set movement pair
    vm.store.move_pair(("A", "B"))
    # Set distance
    vm.store.move_calibration(10)
    # Move distance at speed
    await move_degrees(vm, math.floor(clamp((10 / vm.store.move_calibration()) * 360, -3600000, 3600000) + 0.5), (25, 75))
    # Move distance at speed
    await move_degrees(vm, 360, (-50, 50))
    # Move distance at speed
    await move_ms(vm, 1000, (0, 100))
    # Start dual speed
    move_start(vm, [75, -25])
    # Steer distance at speed
    await move_degrees(vm, math.floor(clamp((20 / vm.store.move_calibration()) * 360, -3600000, 3600000) + 0.5), from_steering(-50, 75))
    # Steer distance at speed
    await move_degrees(vm, 360, from_steering(0, -50))
    # Steer distance at speed
    await move_ms(vm, 2000, from_steering(-100, 25))
    # Start steer at speed
    move_start(vm, from_steering(50, 75))
    # Start dual power
    vm.system.move.on_pair(*vm.store.move_pair()).start_at_powers(-75, -25)
    # Start steer at power
    vm.system.move.on_pair(*vm.store.move_pair()).start_at_powers(*from_steering(-30, 50, True))
    # Movement set stop method
    vm.store.move_stop(1)
    # Movement set acceleration
    vm.store.move_acceleration((100, 100))
    # Control wait until
    while True:
        if vm.store.move_last_status() == INTERRUPTED:
            break
        yield 0

# When program starts
async def stack_3(vm, stack):
    # Led animation
    global g_animation
    brightness = vm.store.display_brightness()
    frames = [hub.Image(convert_animation_frame(frame, brightness)) for frame in g_animation]
    vm.system.display.show(frames, clear=False, delay=125, loop=True, fade=1)
    # Led animation until done
    global g_animation_1
    brightness_1 = vm.store.display_brightness()
    frames_1 = [hub.Image(convert_animation_frame(frame_1, brightness_1)) for frame_1 in g_animation_1]
    await vm.system.display.show_async(frames_1, clear=False, delay=100, loop=False, fade=5)
    # Led image for
    await vm.system.display.show_async(hub.Image(convert_image("9909999099000009000909990", vm.store.display_brightness())), clear=True, delay=2000)
    # Led image
    vm.system.display.show(hub.Image(convert_image("9909999099000009000909990", vm.store.display_brightness())), clear=False)
    # Led text
    await vm.system.display.write_async("Hello")
    # Display off
    hub.display.clear()
    # Led set brightness
    vm.store.display_brightness(75)
    # Led on
    hub.display.pixel(0, 4, 6)
    # Led rotate direction
    rotate_orientation("counterclockwise")
    # Led rotate orientation
    set_current_orientation_from_ui_value("1")
    # Center button light
    color = 9
    if color in [4, 5]:
        color = color + 1
    hub.led(color)
    # Ultrasonic light up
    port = getattr(hub.port, "A", None)
    if getattr(port, "device", None) and is_type("A", 62):
        port.device.mode(5, bytes("".join([chr(percent_to_int(math.floor(clamp(to_number(p), 0, 100) + 0.5), 87)) for p in "100 100 0 0".split()]), "utf-8"))

# When program starts
async def stack_4(vm, stack):
    # Play sound until done
    await vm.system.sound.play_async("/extra_files/Tadaa", freq=pitch_to_freq(vm.store.sound_pitch(), 12000, 16000, 20000))
    # Play sound
    vm.system.sound.play("/extra_files/Tadaa", freq=pitch_to_freq(vm.store.sound_pitch(), 12000, 16000, 20000))
    # Beep for time
    await vm.system.sound.beep_async(60, 200)
    # Beep
    vm.system.sound.beep(60, 32767)
    yield 10
    # Stop sound
    vm.system.sound.stop()
    await vm.extensions["sound"].stop_all()
    # Sound changeeffectby
    vm.store.sound_pitch(math.floor(clamp(vm.store.sound_pitch() + 10, -360, 360) + 0.5))
    # Sound changeeffectby
    vm.store.sound_pan(math.floor(clamp(vm.store.sound_pan() + -10, -100, 100) + 0.5))
    # Sound changeeffectby
    vm.store.sound_pitch(math.floor(clamp(vm.store.sound_pitch() + -120, -360, 360) + 0.5))
    # Sound seteffectto
    vm.store.sound_pan(-75)
    # Sound cleareffects
    vm.store.sound_pitch(0)
    vm.store.sound_pan(0)
    # Sound changevolumeby
    new_volume = math.floor(clamp(vm.system.sound.get_volume() + -10, 0, 100) + 0.5)
    vm.system.sound.set_volume(new_volume)
    vm.store.sound_volume(new_volume)
    # Sound setvolumeto
    volume = 75
    vm.system.sound.set_volume(volume)
    vm.store.sound_volume(volume)
    # Data setvariableto
    vm.vars["Var"] = (STRING, str(vm.store.sound_volume()))

# When color
async def stack_5(vm, stack):
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, 0)

def stack_condition(vm, stack):
    sensor_value = get_sensor_value("A", 0, -1, (61,))
    if sensor_value is None:
        sensor_value = -1
    return 9 == sensor_value

# When pressed
async def stack_6(vm, stack):
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, 0)

def stack_condition_1(vm, stack):
    return get_sensor_value("A", 1, 0, (63,)) == 1

# When pressed
async def stack_7(vm, stack):
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, 0)

def stack_condition_2(vm, stack):
    return get_sensor_value("A", 0, 0, (63,)) > 5

# When pressed
stack_condition_generator_1 = None
async def stack_8(vm, stack):
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, 0)

def stack_condition_3(vm, stack):
    global stack_condition_generator_1
    if stack_condition_generator_1 == None:
        stack_condition_generator_1 = vm.system.callbacks.custom_sensor_callbacks.is_less_than("A", 1, 0, (63,), 1)
    if next(stack_condition_generator_1):
        stack_condition_generator_1 = None
        return True
    return False

# When pressed
stack_condition_generator_2 = None
async def stack_9(vm, stack):
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, 0)

def stack_condition_4(vm, stack):
    global stack_condition_generator_2
    if stack_condition_generator_2 == None:
        stack_condition_generator_2 = vm.system.callbacks.custom_sensor_callbacks.did_change("A", 4, 0, (63,), 5)
    if next(stack_condition_generator_2):
        stack_condition_generator_2 = None
        return True
    return False

# When distance
async def stack_10(vm, stack):
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, 0)

def stack_condition_5(vm, stack):
    sensor_value_1 = get_sensor_value("A", 0, 200, (62,))
    if sensor_value_1 is None:
        sensor_value_1 = 200
    return sensor_value_1 < 50

# When orientation
async def stack_11(vm, stack):
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, 0)

# When gesture
async def stack_12(vm, stack):
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, 0)

# When button
async def stack_13(vm, stack):
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, 0)

# When condition
async def stack_14(vm, stack):
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, 0)

def stack_condition_6(vm, stack):
    return compare(get_variable(vm, STRING, "Var"), "100") == 0

# Event whenbroadcastreceived
async def stack_15(vm, stack):
    # Event broadcast
    vm.broadcast("message1")
    yield
    # Event broadcastandwait
    stacks = vm.broadcast("message1")
    while any([s.is_active() for s in stacks]):
        yield

# When timer
async def stack_16(vm, stack):
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, 0)

def stack_condition_7(vm, stack):
    return compare(vm.get_time() / 1000, 1) > 0

# When program starts
async def stack_17(vm, stack):
    # Control wait
    yield 3000
    # Control wait until
    while True:
        if compare(get_variable(vm, STRING, "Var"), "100") == 0:
            break
        yield 0
    # Control repeat
    for _ in range(10):
        # Data setvariableto
        vm.vars["Var"] = (NUMBER, 0)
        yield
    # Control forever
    while True:
        # Data setvariableto
        vm.vars["Var"] = (NUMBER, 0)
        yield

# When program starts
async def stack_18(vm, stack):
    # Control repeat until
    while not (compare(get_variable(vm, STRING, "Var"), "100") == 0):
        # Data setvariableto
        vm.vars["Var"] = (NUMBER, 0)
        yield
    # Control if
    if compare(get_variable(vm, STRING, "Var"), "100") == 0:
        # Data setvariableto
        vm.vars["Var"] = (NUMBER, 0)
    # Control if else
    if compare(get_variable(vm, STRING, "Var"), "100") == 0:
        # Data setvariableto
        vm.vars["Var"] = (NUMBER, 0)
    else:
        # Data setvariableto
        vm.vars["Var"] = (NUMBER, 1)
    # Fork
    done = False
    async def fork():
        # Data setvariableto
        vm.vars["Var"] = (NUMBER, 0)
        nonlocal done
        done = True
    stack.fork("fork", fork())
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, 1)
    while not done:
        yield
    # Stop other stacks
    if hasattr(vm, "reset_devices"):
        vm.reset_devices()
    vm.stop_stacks(except_stack=stack)
    # Stop
    if hasattr(vm, "reset_devices"):
        vm.reset_devices()
    vm.stop_stacks()
    while True:
        yield

# When program starts
async def stack_19(vm, stack):
    # Stop
    stack.stop()
    while True:
        yield

# When program starts
async def stack_20(vm, stack):
    # Stop
    vm.stop()

# When program starts
async def stack_21(vm, stack):
    # Control wait until
    while True:
        sensor_value_2 = get_sensor_value("A", 0, -1, (61,))
        if sensor_value_2 is None:
            sensor_value_2 = -1
        option = 9
        if (option == sensor_value_2) or ((option in (3, 4)) and (sensor_value_2 in (3, 4))):
            break
        yield 0
    # Data setvariableto
    sensor_value_3 = get_sensor_value("A", 0, -1, (61,))
    if sensor_value_3 is None:
        sensor_value_3 = -1
    vm.vars["Var"] = (NUMBER, sensor_value_3)
    # Control wait until
    while True:
        if get_sensor_value("A", 1, -1, (61,)) > 75:
            break
        yield 0
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, get_sensor_value("A", 1, -1, (61,)))
    # Control wait until
    while True:
        sensor_value_4 = get_sensor_value("A", 0, 200, (62,))
        if sensor_value_4 is None:
            sensor_value_4 = 200
        if sensor_value_4 < 50:
            break
        yield 0
    # Data setvariableto
    sensor_value_5 = get_sensor_value("A", 0, 200, (62,))
    if sensor_value_5 is None:
        sensor_value_5 = 200
    vm.vars["Var"] = (NUMBER, sensor_value_5)
    # Data setvariableto
    gesture = hub.motion.gesture()
    vm.vars["Var"] = (STRING, str(gesture if (gesture is not None) else -1))
    # Control wait until
    while True:
        if hub.motion.gesture() == 2:
            break
        yield 0
    # Control wait until
    while True:
        if hub.motion.orientation() == 3:
            break
        yield 0
    # Data setvariableto
    vm.vars["Var"] = (STRING, get_sensor_value("orientation", 1, None, ()))
    # Reset yaw
    hub.motion.yaw_pitch_roll(0)
    yield 100
    # Control wait until
    while True:
        if not hub.button.left.is_pressed():
            break
        yield 0
    # Data setvariableto
    values = get_sensor_value("position", 0, 0, ())
    vm.vars["Var"] = (NUMBER, values[1])
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, vm.get_time() / 1000)
    # Reset timer
    vm.reset_time()
    # Data setvariableto
    sensor_value_6 = get_sensor_value("A", 2, -1, (61,))
    if sensor_value_6 is None:
        sensor_value_6 = -1
    vm.vars["Var"] = (STRING, str(math.floor((sensor_value_6 * 0.249) + 0.5)))
    # Control wait until
    while True:
        if get_sensor_value("A", 1, 0, (63,)) == 1:
            break
        yield 0
    # Control wait until
    while True:
        if get_sensor_value("A", 0, 0, (63,)) > 5:
            break
        yield 0
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, get_sensor_value("A", 0, 0, (63,)))
    # Data setvariableto
    values_1 = get_sensor_value("accelerometer", 0, (0, 0, 0), ())
    vm.vars["Var"] = (NUMBER, values_1[1])
    # Data setvariableto
    values_2 = get_sensor_value("gyroscope", 0, (0, 0, 0), ())
    vm.vars["Var"] = (NUMBER, values_2[2])
    # Color sensor set mode
    device = g_get_device("A", 61)
    if device:
        device.mode(_DEFAULT_MODE[61])
    # Control wait until
    while True:
        device_1 = g_get_device("A", 61)
        if (device_1.get()[0] if device_1 else 0) > 25:
            break
        yield 0
    # Data setvariableto
    device_2 = g_get_device("A", 61)
    vm.vars["Var"] = (NUMBER, device_2.get()[0] if device_2 else 0)
    # Data setvariableto
    vm.vars["Var"] = (NUMBER, util.sensors.get_type("A"))

# Radiobroadcast when ireceive radio signal hat
async def stack_22(vm, stack):
    # Data setvariableto
    vm.vars["Var"] = (STRING, str(vm.extensions["radiobroadcast"].value(3065852031)))
    # Data setvariableto
    result = ""
    port_1 = getattr(hub.port, "A", None)
    if getattr(port_1, "device", None) is not None:
        try:
            modes = port_1.device.mode()
            results = port_1.device.get(0)
            index = modes.index((1, 2))
            result = results[index]
        except ValueError:
            pass
    vm.vars["Var"] = (STRING, result)
    # Debug debug port mode set data command
    try:
        port_2 = getattr(hub.port, "A", None)
        if getattr(port_2, "device", None) is not None:
            port_2.device.mode(1, bytes("".join([chr(math.floor(clamp(to_number(p_1), 0, 255) + 0.5)) for p_1 in "2 3".split()]), "utf-8"))
    except ValueError:
        pass
    # Debug debug port set mode command
    try:
        port_3 = getattr(hub.port, "A", None)
        if getattr(port_3, "device", None) is not None:
            port_3.device.mode(1)
    except ValueError:
        pass
    # Debug debug port set pwm command
    try:
        port_4 = getattr(hub.port, "A", None)
        if port_4 is not None:
            port_4.pwm(30)
    except ValueError:
        pass

# When program starts
async def stack_23(vm, stack):
    # Data setvariableto
    random = urandom.randint(1, 10)
    vm.vars["Var"] = (NUMBER, random)
    # Control wait until
    while True:
        if -10 <= get_variable(vm, NUMBER, "Var") <= 10:
            break
        yield 0
    # Control wait until
    while True:
        needle = "vent"
        haystack = get_variable(vm, STRING, "Var")
        contains = haystack.lower().find(needle.lower()) >= 0
        if to_boolean(contains):
            break
        yield 0
    # Radiobroadcast broadcast radio signal with value command
    await vm.extensions["radiobroadcast"].broadcast(3065852031, "Hello")

def setup(rpc, system, stop):
    vm = VirtualMachine(rpc, system, stop, "8jrFGmOX9_Z8EwjUn0Y2")

    vm.vars["Var"] = (NUMBER, 73)
    vm.extensions["sound"] = SoundExtension(rpc)
    vm.extensions["radiobroadcast"] = RadioBroadcastExtension(rpc, vm)

    vm.register_on_start(".9YvcSC02j3G/p.ID83[", stack_1)
    vm.register_on_start("nCj5nJ87yi|oBQuD-;iG", stack_2)
    vm.register_on_start("2,?uv@Mf?5I#{NgCzqbO", stack_3)
    vm.register_on_start("DYmOnnWBo6YC^Fw9Zq-{", stack_4)
    vm.register_on_condition("vv$@MbRjJ0F$fQ4f4E6A", stack_5, stack_condition)
    vm.register_on_condition("_kxt#ou}kjMOEmFE/V][", stack_6, stack_condition_1)
    vm.register_on_condition("p@344|J2e_ZmIM^0)?2e", stack_7, stack_condition_2)
    vm.register_on_condition("lnNVET8rvvq|W+)kuaQo", stack_8, stack_condition_3)
    vm.register_on_condition("nX?M(wo,Lt1MRs7h^p{j", stack_9, stack_condition_4)
    vm.register_on_condition("|BLk#,gNs!rQqQj)=X!S", stack_10, stack_condition_5)
    vm.register_on_orientation("ZKmw2)AQ}LNh8!*$c2^4", stack_11, 3)
    vm.register_on_gesture("^e@qsTs0j(5kr0NXiK%m", stack_12, 2)
    vm.register_on_button("M=Kk|8hOXT.l6f`2}Fzy", stack_13, "left", "released")
    vm.register_on_condition("v03DMbq0(H/(A*kSmMa@", stack_14, stack_condition_6)
    vm.register_on_broadcast("3B|dT%P$IB|{37D.mpu=", stack_15, "message1")
    vm.register_on_condition("eTV.ul.Tz1=qK|]F)V7E", stack_16, stack_condition_7)
    vm.register_on_start("0fHR$tdSV)nE.(-t$S{D", stack_17)
    vm.register_on_start("5z(wREuSH1E8t}ftq[1Z", stack_18)
    vm.register_on_start("dOdh]D_iR-dg/4=pB#V_", stack_19)
    vm.register_on_start("awbyPwT?~(i*+bnToH-%", stack_20)
    vm.register_on_start("igNbrp*uP46+3og|(P3R", stack_21)
    vm.extensions["radiobroadcast"].register(3065852031, stack_22, "G,dz/xVo6cfxEQX5]yeq")
    vm.register_on_start("OpUA1P|,pBqV3Xj^ycUy", stack_23)

    vm.extensions["radiobroadcast"].register(3065852031)

    return vm
