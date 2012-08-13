verbose = False
try:
    from rtcmix import *
    import rtcmix as commands
    verbose = False
except ImportError:
    from dummy import *
    import dummy.commands as commands
    verbose = True