""" A recursive algorithm which sprouts a process within itself.
This creates a sort of sonic fractal."""

from oort import *
control_rate(20000)

print_off()

# Be careful with this one...recursive algorithms can blow up easily!
# Avoid setting the recursion_depth or sustain too high, or the decay_exponent too low.
w = WAVETABLE()
env = maketable('window', 1000, 'hanning')

pattern = 0,2,1,1.5,0
recursion_depth = 5
base_amp = 2000
base_freq = 440
dur_mult = 1.
sustain = 1.
decay_exponent = 1.

# Try these settings:

"""pattern = 1,0
recursion_depth = 10
base_amp = 3000
base_freq = 220
dur_mult = 2
sustain = 0.5
decay_exponent = 0.3"""

"""pattern = 0,1,1.5,0
recursion_depth = 5
base_amp = 500
base_freq = 440
dur_mult = 0.25
sustain = 2.
decay_exponent = 0.02"""

def fractal(pitch, level):
    decay = 1./(level+1)**decay_exponent
    if level == recursion_depth:
        return
    dur = dur_mult*decay
    w.dur=dur*sustain
    w.amp = base_amp * decay * env
    for mult in pattern:
        w.pitch = pitch * (1+mult*decay)
        w.play()
        sprout(fractal, w.pitch, level+1)
        wait(dur)

fractal(base_freq,0)