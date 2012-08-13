"""More plucking than a 7th-grade orchestra.

Provides a simple example of different processes controlling different
aspects by taking advantage of Oort's chronological processing."""

import oort
from random import choice, randint

chord = [x+48+12*octave for x in (0,4,7,11) for octave in 0,1,2,3,4]
playing = True

oort.bus_config('START', 'aux 0-1 out')
oort.bus_config('REVERBIT', 'aux 0-1 in', 'out 0-1')

def loop():
    start = oort.START()
    start.amp = 1000
    while playing:
        dur = randint(100, 200) * 0.001
        start.dur=dur*3
        start.pitch=oort.pchcps(oort.mtof(choice(chord)))
        start.play()
        oort.wait(dur)


def change_chord():
    global chord
    while playing:
        oort.wait(choice((4,6)))
        chord = [x+randint(-1,1) for x in chord]

def end_piece():
    oort.wait(30)
    global playing
    playing = False

oort.REVERBIT(0, 0, 30, amp=1., rvbtime=10.,
            rvbamt=1., chan0delay=.06, filtfreq=1200)

oort.sprout(change_chord)
oort.sprout(end_piece)

for i in xrange(10):
    oort.sprout(loop)