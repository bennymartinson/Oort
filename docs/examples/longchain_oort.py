"""An Oortized version of John Gibson's longchain.py sample script.
While this script is about the same length as the original, it shows several
of Oort's features in action, although its advantages here are less clear.
Try uncommenting some of the lines below, or testing out choral.py, 
fractal.py, or gallop.py for some particularly Oortish techniques."""

from oort import *
from random import random as random_percent, choice

#print_off()

bus_config("WAVETABLE", "aux 0-1 out")
bus_config("FLANGE", "aux 0-1 in", "aux 10-11 out")
bus_config("JDELAY", "aux 10-11 in", "aux 4-5 out")
bus_config("REVERBIT", "aux 4-5 in", "out 0-1")

totdur = 30
masteramp = 1.0
atk = 2; dcy = 4

# ---------------------------------------------------------------- synth ---
notedur =  0.10
incr = notedur + 0.015
      
def play_synth():
    w = WAVETABLE()
    
    notes = [5.00, 5.001, 5.02, 5.03, 5.05, 5.07, 5.069, 5.10, 6.00]
    transposition = 2.00    # try 7.00 also, for some cool aliasing...
    
    # try uncommenting the following lines to apply some neat behaviors...
    #w.apply_behaviors(Portamento(amt=0.018))
    #w.apply_behaviors(Humanize(time_variance=0.02))
    #w.apply_behaviors(Shimmer(amt=0.12))
    #w.apply_behaviors(Shimmer(amt=2.), Portamento(amt=0.05))
    
    w.apply_behaviors(ADSR(a=0.005, d=0.095, s=0, r=0),
                      Humanize(amp_variance=4,  # vary by 6 decibels on either side
                               pan_variance=0.5)) # vary pan by .5 on either side)

    w.set(dur=notedur,
          amp=ampdb(85),
          min_control_rate = 20000, # need high control rate for short synth notes
          wavetable = maketable("wave", 10000, 1, .9, .7, .5, .3, .2, .1, .05, .02))
    
    while current_time() < totdur:
        w.pitch = cpsoct(octpch(choice(notes)) + octpch(transposition))
        w.pan = random_percent()
        w.play()
        wait(incr)

sprout(play_synth)

# for the rest
control_rate(500)

# --------------------------------------------------------------- flange ---
f = FLANGE()

lowpitch = 5.00
maxdelay = 1.0 / cpspch(lowpitch)
wavetabsize = 10000
wavet = maketable("wave", wavetabsize, "sine")

f.set(dur=totdur, amp=masteramp, resonance=0.3,
      maxdelay=maxdelay, moddepth=90, modrate=0.08,
      signalmix=0.5, flangetype='IIR', inputchan=0,
      pan=1, ringdowndur=0, modwavetable=wavet)
f.play()

lowpitch += 0.07
maxdelay = 1.0 / cpspch(lowpitch)
wavet = maketable("wave3", wavetabsize, 1, 1, -180)

f.set(maxdelay=maxdelay, modwavetable=wavet,
      inputchan=1,  pan=0)
f.play()

# ---------------------------------------------------------------- delay ---
ringdur = 2.0

def delay():
    deltime = notedur * 2.2
    
    j = JDELAY()
    j.apply_behaviors(ADSR(a=atk, d=1, s=1, r=dcy))
    j.set(dur=totdur, amp=masteramp, delaytime = deltime, 
          feedback=0.7, ringdowndur=ringdur, filtfreq=0,
          sigmix=0.12, inputchan=0, pan=1)
    j.play()
    
    wait(0.02)
    j.set(inputchan=1, pan=0)
    j.play()

sprout(delay)

# --------------------------------------------------------------- reverb ---
r = REVERBIT()

r.set(dur=totdur+ringdur,
      amp=masteramp,
      rvbtime = 1.0,
      rvbamt = 0.3,
      chan0delay = 0.05,
      filtfreq = 0)

r.play()

