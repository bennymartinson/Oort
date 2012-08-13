""" Quickstart guide 1: Welcome to Oort! """

# Welcome to Oort, an Object-Oriented library for RTcmix!

# Oort offers several tools that offer an alternative way to use RTcmix.
# RTcmix instruments are encapsulated in objects of the exact same names, 
# allowing them to be treated in an object-oriented fashion if desired.
# However, Oort tries to emulate RTcmix as closely as possible, so any 
# PYCMIX code that runs using the "rtcmix" library will run identically
# using the "oort" library.  Oort offers a number of features, which for the
# most part can be used independently of each other.  You can load the oort 
# library to use all, some, or none of Oort's extra features.  The extra
# layers make it a little slower than the rtcmix library, but the difference
# is unlikely to get in your way.

# This code in this file is perfectly valid PYCMIX code, which works equally 
# well in Oort. Try replacing "from oort" below to "from rtcmix" and run this 
# script again. It works exactly the same! Now, change it back.

from oort import *

# Once importing from oort again, try commenting out the two lines below.
# Oort offers the option of lazy loading.  If you haven't already loaded an 
# instrument, it will load automatically once it's needed.  If you haven't
# called rtsetparams before your first instrument call, it will be called
# with default parameters of 44100, 2.  Therefore, the following two lines
# are no longer technically necessary in Oort.

rtsetparams(44100, 2)
load('WAVETABLE');


# Let's go up a C Major scale:

outsk = 0
dur = 0.5
pitches = 8., 8.02, 8.04, 8.05, 8.07, 8.09, 8.11, 9.

for pitch in pitches:
    WAVETABLE(outsk, dur, 10000, cpspch(pitch), 0.5)
    outsk += dur