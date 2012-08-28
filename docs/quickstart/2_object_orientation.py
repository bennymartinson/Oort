""" Quickstart guide 2: Object Orientation """

from oort import *

# Oort instrument wrappers are actually objects, meaning you can treat your
# instruments as either functions or objects.


# Running an oort instrument wrapper as a function works exactly like
# standard PYCMIX:

bvenv = maketable("line", 'nonorm', 1000, 0,0., 1,0.5, 9,0.5, 10,0)
bowpressenv = 1.
bowposenv = 0.75
vibwave = maketable("wave", 1000, "sine")
MBOWED(0, 3, 5000, cpspch(8.00), 5,7, 0.02, 0.5, bowvelenv, 
       bowpressenv, bowposenv, vibwave)

# Each instrument in Oort is given default parameters for outskip, duration,
# amplitude, pitch, and pan.  So you really only need to pass in the values
# that depart from Oort's defaults.  You can do this with keyword arguments:

MBOWED(dur=3, amp=5000, pitch=cpspch(8.10), bowvelenv=bowvelenv, 
       bowpressenv=bowpressenv, bowposenv=bowposenv)

# Arguments are named in the Oort instrument wrappers, so if you are using a 
# smart Python integrated development environment like PyDev for Eclipse, 
# instrument parameters will automatically pop up, so you never have to 
# remember the argument names or their order!


# To run an Oort instrument wrapper as an object, save the result of an
# instrument call to a variable.  An instrument instantiated with no 
# parameters will not play until you call play() manually.

bow = MBOWED()
# you can set parameters using dot notation:
bow.dur = 3
# or set several at once using the object's set() method:
bow.set(pitch=cpspch(9.04), amp=2000, vibfreqlo=5, vibreqhi=7)
bow.set(vibdepth=0.02, bowvelenv=bowvelenv, bowpressenv=bowpressenv)
bow.set(bowposenv=bowposenv)
bow.play()

# now that our instrument is saved to a variable, we can play it over,
# changing only the variables desired.
bow.pitch = cpspch(9.08)
bow.play()

# we can also chain methods:
bow.set(pitch=cpspch(10.01)).play()

# OK, gotta resolve.  let's save some space:
bow.set(outsk=2.7, dur=4, pitch=cpspch(8.05)).play()
bow.set(pitch=cpspch(8.09)).play().set(pitch=cpspch(9.04)).play()
bow.set(pitch=cpspch(9.07)).play().set(pitch=cpspch(10.00)).play()
