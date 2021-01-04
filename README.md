# Advanced Python for Mindstorms Robot Inventor

## About this repository

### What is this about

This repository contains technical information and open source code for advanced
[Python](http://www.python.org) programming of [Mindstorms Robot Inventor
(51515)](http://www.lego.com/product/51515) LEGO set. Due to shared hardware and software internals,
most information and code presented here should also be applicable to the [Spike Prime
(45678)](http://www.lego.com/product/45678) set.

If you are disappointed by the limited possibilities offered by the official Python support in the
Mindstorms Inventor mobile app
([Android](http://play.google.com/store/apps/details?id=com.lego.retail.mindstorms) or
[iOS](http://apps.apple.com/app/lego-mindstorms-inventor/id1515448947)) or desktop software
([Windows](http://www.microsoft.com/en-us/p/lego-mindstorms-robot-inventor/9mtq0n7w1d6x) or
[MacOS](http://apps.apple.com/app/lego-mindstorms-inventor/id1515448947)), this website is for you.
We will exploit the fact that the new Mindstorms brick runs [Micropython](http://micropython.org)
natively. You'll quickly be able to do more with Python than with Word Blocks (in fact
[Scratch](http://scratch.mit.edu)) programs, not less.

This site is not affiliated with the LEGO Group. Any information or code presented here might brick
(no pun intended) your Mindstorms hub. So use it at your own risk, but feel free to share your
experience and contribute.

### What is this *not* about

We do not intend to cover the [Mindstorms EV3 (31313)](http://www.lego.com/product/31313) set. Since
[Micropython firmware from Pybricks](http://pybricks.github.io/ev3-micropython) is avalable (and
even officially supported by LEGO) for it, some general information and techniques presented here
might also be applicable to EV3 users using that firmware. Despite this, there are big architectural
differences between EV3 and Robot Inventor (in fact, the [EV3 Intelligent
Brick](http://www.lego.com/product/45500) is much more powerful than the new Mindstorms brick in
many aspects), so we recommend official and other online resources focusing on EV3 for developers
using that set.

Similarly, while [Micropython firmware from Pybricks](http://pybricks.com) can also be used for LEGO
Powered Up hubs like the [Move Hub](http://www.lego.com/product/88006) (part of the [Boost Creative
Toolbox (17101)](http://www.lego.com/product/17101) set), the [City
Hub](http://www.lego.com/product/88009) or the [Technic Hub](http://www.lego.com/product/88012)
(present in many sets with different motor configurations),
those are generally intended for remote control by a smart device rather than running user code and
so are much less powerful. Running user code on those also requires flashing custom firmware, which
comes with its pros and cons.

For all Powered Up hubs remote control via BluetoothLE is possible. This led to creation of
libraries like [BrickNil](http://pypi.org/project/bricknil) or
[pylgbst](http://github.com/undera/pylgbst). While remote control is also possible with the new
Mindstorms hub (called *streaming* mode), reading the sensors and driving motors on the device is
better from latency perspective, so we will focus on it first and look for advanced remote control
options next.

## Getting started

### Background

Mindstorms Robot Inventor hub is running a Micropython "operating system". It includes drivers to
control sensors and motors, a small Python runtime and small set of libraries for common operations
that range from basic file I/O and communication with hub compoents to JSON serialization or
compression.

Micropython can be regarded as a limited and customized version of Python, while Micropython version
run on the hub can be regarded as a limited and customized version of universal Micropython.
Nevertheless, it's still pretty powerful, as it offers asychronous programming and Bluetooth
connectivity, for example. Furthermore, LEGO implemented a bunch of libraries, wrappers and logic
to support its robotic platform and software. The reasonably documented and officially offered
API is pretty primitive, but internally, while somewhat messy, it is pretty rich.

### Concurrency model

Micropython is single-threaded, but has a concept of coroutines which enable cooperative
multi-tasking. Unfortunately, the standard uasyncio library is not included in the firmware, but one
can create and use coroutines using the `async`/`await` syntax.

Mindstorms hub provides its own event loop that is started when the hub is started. This allows
scheduling coroutines that can yield when they await a certain condition and have other code
executed in the meantime.

### Interaction between the app and the hub

When the Mindstorms Inventor app is used, it allows the user to create and upload programs, which
are then executed on the hub. Even when blocks are used, they are internally translated into Python
which is then executed on the hub. While the app the the hub are connected, the hub sends telemetry
back to the app, so that execution can be monitored.

Some functionality requires a remote control (called *streaming*) mode instead, which allows the app
to remotely control the hub. For example, when a keyboard or a game controller event is used, the
app will not send the code which responds to the event to the hub, but will directly steer lights or
motors using the cable or Bluetooth connection. In full streaming mode, all code will be running in
the app and can be changed dynamically in the app while being executed.

Some functionality is provided by the app. For example some sounds or music are played by the app
itself. If the hub is connected to the app, Python code will invoke functionality in the app via
a Remote Procedure Call (RPC) protocol.

### How programs are executed

After the hub is started and the execution environment (runtime) is initialized, the main event loop
is started. Initially it runs two main internal programs: the "ui" program responsible for selection
and execution of user programs from the hub and the RPC handler responsible for remote control from
the Mindstorms Inventor app and the telemetry.

The hub distinguishes Word Blocks and Python user programs, even though both result in Python code
in the end. They are executed when the program is selected on the hub using the buttons or where an
instruction to execute a program is sent from the app. This runs user code until stopped or until
an error occurs.

Word Block programs are provided with setup environment, so they can construct a "virtual machine"
(VM) that builds on top of the event loop, allows convenient registration of event handlers,
integrates with the RPC system and provides mid-level program building blocks.

Python programs are executed directly. A simple synchronous API is provided through the `MSHub` and
other classes, but it is far from obvious how to react to events or execute parts of program in
parallel.

## My first program

### Synchronous "Hello world"

Using the official documentation we can produce the following simple program that prints "Hello
world" on the light matrix:

```python
import mindstorms

hub = mindstorms.MSHub()
hub.light_matrix.write("Hello world")
```

It is cool, but not really extensible. What if we wanted to play a sound on the hub (there does not
even seem to be a documented API for this) while displaying the message and stop any of this when a
button is pressed? It is possible using blocks, so must be possible using Python.

### Asynchronous "Hello world"

Let's mimic the code generated from Word Blocks (we'll discuss later how to get it) doing the same:

```python
import runtime
import sys
import system

async def main(vm, stack):
    await vm.system.display.write_async("Hello world")
    vm.stop()

def setup(rpc, system, stop):
    vm = runtime.VirtualMachine(rpc, system, stop, "HelloWorld")
    vm.register_on_start("main", main)
    return vm

class RPC:
    def emit(self, op, id):
        pass

setup(RPC(), system.system, sys.exit).start()
```

The `setup` function creates a virtual machine (VM) and registers program components. In our
example the `main` function will be executed on start. The RPC class fakes the RPC part needed for
execution reporting, we'll see later how to set it up properly.

The last line is the magic that invokes the setup, linking the VM to the system environment. After
setting up the VM up, we start it, so that the event loop can start executing our program. We need
to do this manually, since such setup won't be invoked automatically for Python programs.

The actual program lives in the asynchronous `main` function, so we can invoke and await coroutines
like the `write_async` one. Since we're given a handle to the VM, we can stop it after the
`write_async` operation completes, effectively completing our user program and returning control to
the built-in "ui" program.

### Full-blown "Hello world"

So let's make this example a bit more interesting by doing two things (light and sound) in parallel
and allowing asynchronous cancelation:

```python
import hub
import runtime
import sys
import system

async def run(vm, stack):
    vm.broadcast("run")

async def display(vm, stack):
    await vm.system.display.write_async("Hello world")

async def sound(vm, stack):
    await vm.system.sound.play_async("/extra_files/Hello")
    await vm.system.sound.play_async("/extra_files/Celebrate")

async def cancel(vm, stack):
    vm.stop_stacks(except_stack=stack)
    hub.display.clear()
    hub.sound.beep(0, 0)

def setup(rpc, system, stop):
    vm = runtime.VirtualMachine(rpc, system, stop, "HelloWorld")
    vm.register_on_start("run", run)
    vm.register_on_broadcast("display", display, "run")
    vm.register_on_broadcast("sound", sound, "run")
    vm.register_on_button("left_button", cancel, "left", "pressed")
    vm.register_on_button("right_button", run, "right", "pressed")
    return vm

class RPC:
    def emit(self, op, id):
        pass

setup(RPC(), system.system, sys.exit).start()
```
