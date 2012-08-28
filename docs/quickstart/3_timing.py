""" Quickstart guide 3: Timing"""

from oort import *
control_rate(15000)
print_off()

# Oort offers an alternative, wait-based approach to timing inspired by, 
# but departing from languages like ChucK and Common Music.  Oort's schedule 
# module uses a system of threads and locks which reorganizes the operation 
# of your code into a chronological sequence.  This simulates threads 
# running and waiting in real-time, but it executes in an instant!

# This is done using an internal moment cursor, which holds the time that is
# "now" in the script. Oort instruments automatically read from this cursor 
# if no outskip is specified.  To get the moment cursor at  any time, call 
# the now() function:

print "time at beginning:", now()

# to wait, just call wait(dur), where dur is the duration to wait in 
# seconds.

# Having to order each event sequentially would not be very fun or useful
# if you have multiple ideas going on at once.  To solve this, Oort lets you
# sprout multiple concurrent processes; that is, functions whose timers
# operate independently of the timers outside of their local scope.  When
# a process is sprouted, the time outside the process remains unchanged.

# Creating and sprouting processes is easy.  Just define a function, then
# call sprout() on the function and pass in its parameters.  For example:

def loop(dur, pan=0.5):
    w.dur = dur * 2
    while True: # repeat forever, unless function returns
        for pitch in 60, 64, 66, 69, 70, 67, 62: # cycle through 7 pitches
            w.pitch = cpsmidi(pitch)
            w.play()
            wait(dur)
            
            if not playing: # We'll come back to this
                return

# setting some variables:
playing = True
w = WAVETABLE()
w.wavetable = maketable('wave', 1000,'buzz')
w.amp = 10000 * maketable('expbrk', 1000, 1,999,0)

# Now you can sprout this function as many times as you'd like, to get some
# complexity:
sprout(loop, 0.2, 0)
sprout(loop, dur=0.3, pan=1)
sprout(loop, dur=0.4, pan=0.3)
sprout(loop, dur=0.5, pan=0.7)

# Even though we've sprouted these processes which do a lot of waiting, our
# time outside these processes is still 0.  See:
print 'Time after sprouting loops:', now()

# Now, the coolest thing about working with code that is processed 
# chronologically is you can now control different musical aspects or ideas
# in different processes. In ordinary procedural code, setting a value down
# here wouldn't affect what's going on in the code above.  But since the 
# code is reorganized chronologically by Oort, any variable we set here at 
# some time t will be available everywhere else in the code that is schedule
# after that time t.

# Here's an example. At 5 seconds in, let's change our WAVETABLE object's
# internal wavetable:

def change_wavetable():
    wait(5)
    w.wavetable = maketable('wave', 1000, 'tri')

sprout(change_wavetable)


# You may have noticed that in the loop function above, the code is on an
# endless loop until the variable "playing" becomes False.  We'd better end
# the loop at some point so your CPU doesn't melt..  Let's wait 10 seconds, 
# then stop the function above.

wait(10)
playing = False