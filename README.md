# Advanced Python for Mindstorms Robot Inventor

## What this repository is about

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
natively. You'll quickly be able to do more with Python than with [Scratch](scratch.mit.edu) block
programs, not less.

This site is not affiliated with the LEGO Group. Any information or code presented here might brick
(no pun intended) your Mindstorms hub. So use it at your own risk, but feel free to share your
experience and contribute.

## What this repository is not about

We do not intend to cover the [Mindstorms EV3 (31313)](http://www.lego.com/product/31313) set. Since
[Micropython firmware from Pybricks](https://pybricks.github.io/ev3-micropython) is avalable (and
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
those are generally intended for remote control by a smart device rather than running user code. And
so are much less powerful and depend on flashing custom firmware, which limits compatibility.
