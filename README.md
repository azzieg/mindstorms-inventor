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
natively. You'll quickly be able to do more with Python than with [Scratch](http://scratch.mit.edu)
block programs, not less.

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
options later.

## Getting started

### Background

Mindstorms Robot Inventor hub is running a Micropython "OS". It includes drivers to control sensors
and motors, a small Python runtime and small set of libraries for common operations that range from
basic file I/O and communication with hub compoents to JSON serialization or compression.

Micropython can be regarded as a limited and customized version of Python, while Micropython version
run on the hub can be regarded as a limited and customized version of universal Micropython.
Nevertheless, it's still pretty powerful, as it offers asychronous programming and Bluetooth
connectivity, for example. Furthermore, LEGO implemented a bunch of libraries, wrappers and logic
to support its robotic platform and software. The reasonably documented and officially offered
API is pretty primitive, but internally, while somewhat messy, it is pretty rich.

### Interaction between the app and the hub

When the Mindstorms Inventor app is used, it allows the user to create and upload programs, which
are then executed on the hub. Even when code blocks are used, they are internally translated into
Python which is then executed on the hub. The hub sends telemetry back to the app, so that execution
can be monitored.

Some functionality requires a remote control (called *streaming*) mode instead, which allows the app
to remotely control the hub. For example, when a keyboard or a game controller event is used, the
app will not send the code which responds to the event to the hub, but will directly steer lights or
motors. In full streaming mode, all code will be running in the app and can be changed dynamically
in the app while being executed.

Some functionality is provided by the app. For example some sounds or music are played by the app
itself. If the hub is connected to the app, Python code will invoke functionality in the app via
a Remote Procedure Call (RPC) protocol.
