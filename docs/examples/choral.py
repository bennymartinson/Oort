"""A simple choral texture."""

import oort
import random
oort.print_off()
oort.control_rate(15000)

playing = True
def play():
    oort.wait(random.choice(range(10))*0.1)
    while playing:
        dur = 2 + random.randint(-10, 10)*.05
        w.dur = dur*random.randint(2,4)
        w.pitch = oort.mtof(random.choice(scale))
        w.play()
        oort.wait(dur)

def control():
    global playing
    global scale
    for _ in xrange(6):
        offset = random.randint(-2,2)
        scale = [x+offset for x in scale]
        oort.wait(20)
    playing = False

w = oort.WAVETABLE()
w.amp = 5000
w.wavetable = oort.maketable('wave', 1000, 1, 0.1)

adsr = oort.ADSR(2, 0.5, 0.5, 2)
shimmer = oort.Shimmer(amt=0.03, count=10)
w.apply_behaviors(shimmer, adsr)

scale = [ p+octave*12 
          for p in 0,2,4,6,7,9,10 
          for octave in 4,5,6 ]
oort.sprout(control)

for _ in range(2):
    oort.sprout(play)