"""A script highlighting Oort's Animation object.

An Animation object controls values over time according to a user-specified
table."""

from oort import *

def timing():
    wait(60)
    global playing
    playing=False

def scale():
    b = RISSETBELL()
    b.dur = 1
    b.apply_behaviors(
              Humanize(time_variance=Ramp(0., 0.01, 30)),
              ADSR(0.01, 0.1, 0.3, 0.1)
              )
    b.pitch = Animation(minval=440, 
                maxval=880, 
                dur=5, 
                table=maketable('line',25 ,0,0, 1,1, 2,0),
                loop=True)
    b.amp = Animation(minval=0., 
                maxval=5000., 
                dur=7, 
                table=maketable('line',25 ,0,0, 1,1, 2,0),
                loop=True)
    
    x=0
    while playing:        
        b.pan=(x%7)%2
        b.play()
        wait((((x%17)%5)%2+1)*0.2)
        x+=1

print_off()
control_rate(15000)

playing=True
sprout(timing)
for _ in xrange(10):
    sprout(scale)
    wait(.5)