Oort
====

An object-oriented wrapper for the [RTcmix](http://rtcmix.org/) language in Python

OVERVIEW
------
Oort is a library designed to help you write powerful, expressive Python code to interface with RTcmix.  It is built entirely on top of the RTcmix library, and is run with the [PYCMIX](http://music.columbia.edu/cmc/RTcmix/use/python.html) executable.

Oort wraps RTcmix's instruments into classes of the same name.  This allows Oort (and you!) to easily extend the behavior of instruments with minimal intrusion into the syntax of the RTcmix language.  In fact, any python code using the 'rtcmix' library should work equally well using the 'oort' library.

However, Oort offers a number of features which allow you to work with RTcmix a bit differently, if you so choose:

<h4>Syntax features</h4>
Oort offers a number of small, but handy features designed to make your RTcmix experience a little smoother.  While it was built specifically for the Eclipse PyDev environment, Oort is designed to help whatever IDE you use with code completion and debugging.

Features include:
* Lazy loading automatically loads instruments the first time they are using, meaning calling load() before your instrument call is optional in Oort.
* Parameters can be entered as either a list of arguments or a list of keyword-argument pairs, or both in the manner Python allows.  For example:
  <pre>NOISE(outsk=0, dur=1, amp=5000, pan=0.5)</pre>
  If you need to know the names of the parameters, you can pull up the internal documentation
  <pre>help(NOISE)</pre>
  Or, to pull up the RTcmix docs online, just call the following in your script or on the PYCMIX or Python [REPL](http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop):
  <pre>docs(NOISE)</pre>
* Each instrument has a number of default values for its parameters including outskip (see Oortian timing below), inskip, pitch, amp, and pan.  This means you can call an instrument with only the parameters you find relevant, for example:
  <pre>NOISE(amp=5000, pan=0.)</pre>
* Oort code will run silently if you run it with python instead of PYCMIX.  This way, you can debug your code in a Python IDE, and a "dummy" RTcmix library will be loaded to keep it from throwing errors.

<h4>Object-oriented features</h4>
Since a call to an Oort instrument actually instantiates an object, you can assign this object to a variable, change parameters, and play it any number of times.  For example, as well as doing this:
<pre>from oort import *
NOISE(0, 1, 5000)</pre>
You can do something like this:
<pre>
from oort import *
n = NOISE()
n.set(dur=1, amp=5000).play()
n.outsk = 2
n.play()
</pre>

<h4>Oortian timing</h4>
Oort allows you to work with a chronological timing paradigm if you so choose.  This works in a way that (sort of) emulates languages like ChucK that sprout concurrent threads that wait and perform actions.

Oort has its own wait() function that progresses time forward, and a sprout() function which creates a thread that controls its own clock. Since PYCMIX code is preprocessed, the wait() function controls the outskip of instrument calls, but does not physically wait any amount of time.

Oort does, however, reorder the operation of the code, using a system of thread locks, so that the code always operates chronologically!  This means if you set a global variable x=4 at time=3 seconds, that variable will be 4 in any other process where time > 3 seconds.  This lets you organize your RTcmix scripts in a very different way.

Here's a quick example.  For a tutorial on timing, check out the Quickstart guide.
<pre>
from oort import *
playing = True
def play():
  w = WAVETABLE()
  w.dur = 0.5
  while playing:
    w.pitch = cpsmidi(pickrand(60, 62, 64, 65, 67))
    wait(0.5)
    w.play()
sprout(play)

def control(wait_time):
  global playing
  wait(wait_time)
  playing = False

sprout(control, wait_time=10)
</pre>


<h4>Behaviors</h4>
Instruments in Oort can be given extra sets of functionality by applying Behavior objects. Oort comes with several useful behaviors built in, and it is simple to build your own.  Built-in behaviors include:
* ADSR, for applying an ADSR envelope to an instrument (that scales correctly to the note duration)
* Jitter, for applying some variance to the pitch of an instrument
* Humanize, for adding random variance to pitch, amplitude, pan, or timing
* Portamento, for automatically sliding between an instrument's successive pitches

For example:
<pre>
from oort import *
w = WAVETABLE()
w.dur = 0.5
w.apply_behaviors(Jitter(amt=0.1), Portamento(amt=0.1), ADSR(a=0.05, d=0.1, s=0.2, r=0.5))
for _ in xrange(20):
  w.pitch = cpsmidi(pickrand(60, 62, 64, 65, 67))
  wait(0.5)
  w.play()
</pre>

<h4>Dynamic Values</h4>
Dynamic Values are as-of-yet underdeveloped but still very useful objects.  A dynamic value can be provided as an instrument or object parameter anywhere a float is expected.  These objects allow the programmer to set up values that change over time, such as ramps or shapes, which are defined by an RTcmix table.

For example, here's a fade-in:
<pre>
from oort import *
w = WAVETABLE()
w.dur = 0.5
w.amp = Ramp(start_val=0, end_val=10000, dur=10)
while current_time() &lt; 10:
  w.pitch = cpsmidi(pickrand(60, 62, 64, 65, 67))
  wait(0.5)
  w.play()
</pre>

<h4>More</h4>
Oort offers several other smaller features, from bus management to RTcmix introspection to custom (composite) instruments. Most of these features are still undocumented, and many more features are planned for future releases.

INSTALLATION
------
To install Oort, navigate to the directory this file is in and call:
<pre>python setup.py install</pre>

...and you're done!  If you have multiple versions of python on your machine, make sure you install setup.py with the same version used to compile PYCMIX, for example:
<pre>/usr/bin/python setup.py install</pre>

USAGE
------
The 'oort' library can be used in python scripts in the same way the 'rtcmix' library is used.  Just import the library like so: 
<pre>import oort</pre>
and the entire RTcmix library–and all of Oort's extra functionality–are loaded into your script! Oort projects are also run the same way, using PYCMIX:
<pre>PYCMIX &lt; sample.py</pre>
If you don't have PYCMIX installed, http://rtcmix.org/ can tell you how to build it.

QUICKSTART
------
For a quickstart tutorial on using Oort, refer to the quickstart files in docs/quickstart/.

THANKS
------
Special thanks go to Joel Matthys for inspiring the idea and Mara Helmuth for introducing me to the world of RTcmix!