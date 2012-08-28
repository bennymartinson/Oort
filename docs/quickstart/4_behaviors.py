""" Quickstart guide 4: Behaviors"""

from oort import *
from random import choice, uniform
print_off()
control_rate(20000)

# The last major component of Oort to explore is Behaviors.  Behaviors are 
# objects which can be applied to instruments to modify their behavior in 
# some way.

# A full list of built-in behaviors can be found in the behaviors module,
# but it's easy to build your own! 

# Let's start with a Portamento behavior.  This, as the name suggests,
# slides between pitches.  It can be applied to any instrument that has a
# p-field enabled pitch parameter.

portamento = Portamento(amt=0.15)

# And let's create a smart-stretching envelope, using the ADSR behavior, 
# which can be applied to any instrument that has a p-field enabled amp
# parameter.

adsr = ADSR(a=0.5, d=0.5, s=0.5, r=0.5)

# Now, we just have to apply these behaviors to an instrument using the 
# apply_behaviors() function:

bwg = MBANDEDWG()
bwg.preset=3
bwg.amp=5000

# try commenting out the following line to hear how much these behaviors
# affected the original instrument.
bwg.apply_behaviors(portamento, adsr)


def play():
    while now() < 15:
        bwg.pitch = cpsmidi(choice([2,9,12,17,23,28,31])+60)
        dur = uniform(0.2,0.4)
        bwg.dur = dur
        bwg.play()
        wait(dur)

sprout(play)

# Let that sink in for 10 seconds:
wait(10)

# Behaviors can be applied and modified at any point.

# Below, we're creating an instance of Oort's RISSETBELL instrument, an 
# additive synthesis instrument based on a PYCMIX score file by John Gibson.

bell = RISSETBELL()
bell.dur=3

# Let's fade the bells in over time using an Oort Ramp DynamicValue object.
# Dynamic values return different numbers over time according to an internal 
# RTcmix table, and can be substituted for floats in arguments to 
# instruments and behaviors.

bell.amp = Ramp(start_val=0, end_val=10000, dur=5)

def bells():
    while now() < 35:
        bell.pitch = cpsmidi(choice([2,9,12,17,23,28,31])+choice([60,72]))
        bell.play()
        wait(0.1)
        
sprout(bells)

# After 5 seconds, let's apply some new behaviors to the Risset bell.
wait(5)

jitter = Jitter(amt=0.1) # random wavering in pitch
humanize = Humanize(pan_variance=0.5) # random imperfections in panning

bell.apply_behaviors(jitter,humanize)

# Now let's fade in lots of randomness in amplitude timing, and pitch:
humanize.amp_variance = Ramp(0, 20, 15)
humanize.time_variance = Ramp(0, 0.1, 15)
humanize.pitch_variance = Ramp(0, 3, 15)

# This quick-start guide just scratched the surface of what you can do with
# Oort.  Check out the samples folder for more demonstration.