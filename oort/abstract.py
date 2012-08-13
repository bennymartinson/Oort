import schedule
import rtcmix_import as rtcmix
#from utilities import *
import animation
import errors

class OortObject(object):
    """Abstract base class for all Oort instruments and behaviors."""
    def __getattribute__(self, *args, **kwargs):
        """When an animation object is accessed, return its number value instead."""
        attr = object.__getattribute__(self, *args, **kwargs)
        if isinstance(attr, animation.Animation):
            return attr.value()
        else:
            return attr

total_instrument_plays = 0

class Instrument(OortObject):
    """Abstract base class for all Oort instruments."""
    outsk=0
    dur=1
    amp=10000
    pitch=440
    pan=0.5
    instrument = None
    loaded = False
    pfields = ()
    min_control_rate = 0
    _prev_control_rate = 0
    
    def __init__(self, args):
        import inspect
        spec = inspect.getargspec(self.__init__)
        argnames = spec[0]
        extra_args = spec[1] # the name of the list
        extra_kwargs = spec[2] # the name of the dict
        if extra_args is not None:
            argnames.append(extra_args)
        if extra_kwargs is not None:
            argnames.append(extra_kwargs)
        play = False
        
        for argname in argnames:
            key = argname.lower() # we don't want to have to remember which case everything is in!
            if argname is 'self':
                continue
            if args[argname] is not None:
                if  argname not in (extra_args, extra_kwargs):
                    play = True
                setattr(self, key, args[argname])
            elif not hasattr(self, key):
                setattr(self, key, None)
        
        if play: # if at least one argument was passed to the constructor
            self.play()
    
    def _passback(self, args):
        Instrument.__init__(self, args)
    
    def set(self, **kwargs):
        """Set several params at once by key and value."""
        for key,val in kwargs.items():
            setattr(self, key, val)
        return self
    
    def _get(self, name):
        """Used to obtain calculated values to be passed to RTcmix instrument.
        
        Uses method get_{value} if this method exists.For example, outsk is modified by get_outsk
        to add the current time to outsk."""
        if hasattr(self, 'get_'+name):
            return getattr(self, 'get_'+name)()
        else:
            return getattr(self, name)
    
    def get_outsk(self):
        return self.outsk + schedule.current_time()
    
    def apply_behaviors(self, *behaviors):
        for behavior in behaviors:
            self.apply_behavior(behavior)
    
    def apply_behavior(self, behavior):
        """Apply a behavior to this instrument.  
        
        This applies each method in the behavior as a decorator to a corresponding method in the instrument."""
        
        if not self.can_apply_behavior(behavior):
            raise errors.OortBehaviorError('This behavior requires a parameter to be pfield-enabled which is not pfield-enabled.  Please try a different behavior, or check that your instrument has the correct pfields parameter set.')
        for var in dir(behavior):
            if (var.startswith('get_') or 
                var in ('_play', '_before_play', '_after_play')):
                # need to call a separate function for closure to capture vars
                self._build_behavior_dispatch(behavior, var)
    
    def can_apply_behavior(self, behavior):
        if not hasattr(behavior, 'required_pfields') or not len(behavior.required_pfields):
            return True
        if not hasattr(self, 'pfields'):
            return False
        for pfield in behavior.required_pfields:
            if pfield not in self.pfields:
                return False
        return True
    
    def _build_behavior_dispatch(self, behavior, var): 
        if hasattr(self, var) and hasattr(getattr(self, var), '__call__'):
            # if self has function with name var, decorate function
            fn = getattr(self, var)
        elif var.startswith('get_'):
            # if var in form get_var, return function getting var from self
            varname = var[4:]
            fn = lambda: getattr(self, varname, 0)
        else:
            # not interested
            return
        
        new_fn = getattr(behavior, var)     
        def _behavior_dispatch(*args):
            return new_fn(self, fn, *args)
        setattr(self, var, _behavior_dispatch)
    
    def play(self):
        """Runs the corresponding RTcmix command.  
        Do not override.  Instead, override _play()"""
        
        self._load()
        
        # Set to default in case it was not already set:
        rtcmix.rtsetparams(44100, 2)
        
        args,keys = self.get_instrument_args()
        
        if rtcmix.verbose:
            print "Calling instrument",self.instrument,"with parameters",args
        
        self._before_play(())
        # Make sure control rate is at least min_control_rate
        self._prev_control_rate = rtcmix.current_control_rate()
        if self._prev_control_rate < self.min_control_rate:
            rtcmix.control_rate(self.min_control_rate)
        
        # Play
        self._play(args,keys)
        
        # Return control rate to prev value.
        if self._prev_control_rate != rtcmix.current_control_rate():
            rtcmix.control_rate(self._prev_control_rate)
        
        self._after_play(())
        
        global total_instrument_plays
        total_instrument_plays+=1
        
        return self
    
    def get_instrument_arg_names(self):
        import inspect
        args = inspect.getargspec(self.__init__)
        return args[0]
    
    def get_instrument_args(self):
        # Read arguments from instrument's __init__() function
        argnames = self.get_instrument_arg_names()
        # Collect list of consecutive non-None parameters
        args = []
        keys = []
        for argname in argnames:
            argname = argname.lower()
            if argname == 'self':
                continue
            arg = self._get(argname)
            if arg is None:
                break; # We hit a None parameter, so can't add more to arg list
            args.append(arg)
            keys.append(argname)
        
        if hasattr(self, 'extra_args'):
            for arg in self.extra_args:
                keys.append('p'+str(len(args)+1)) # just default to calling it p4, p5, etc.
                args.append(arg)
        
        if hasattr(self, 'extra_kwargs'):
            for k,v in self.extra_kwargs.items():
                keys.append(k)
                args.append(v)
        return args, keys
    
    def _play(self, args, keys):
        """Call RTcmix function.
        Override for custom functionality."""
        getattr(rtcmix, self.instrument)(*args)
    
    def _before_play(self, args):
        """ Called once before playing an instrument.
        Override for custom functionality."""
        pass
    
    def _after_play(self, args):
        """ Called once after playing an instrument.
        Override for custom functionality."""
        pass
    
    def _load(self):
        """Load instruments as necessary.
        Override for complex instruments."""
        
        load = getattr(self, 'load', self.instrument)
        if not hasattr(load, '__iter__'):
            load = load,
        for l in load:
            try:
                rtcmix.load(l)
            except:
                raise errors.OortInstrumentError('The package '+str(l)+' does not exist to load in instrument '+str(self.instrument))
    
    def docs(self):
        import webbrowser
        webbrowser.open('http://music.columbia.edu/cmc/RTcmix/docs/instruments/'+self.instrument+'.html')

class Effect(Instrument):
    insk = 0
    amp = 1

class Behavior(OortObject):
    """Abstract behavior class.
    
    Behaviors let one easily apply new functionality to any instrument(s) using function decorators.
    Unlike subclassing an instrument, behaviors are intended to be ignorant of the type of instrument
    to which they are applied, and a single behavior instance can be applied to several instrument
    instances.
    
    See Behavior's subclasses for examples."""
    
    # List of parameters that must be pfield-enabled 
    # in order for this behavior to be set to an instrument.
    required_pfields = () 
    
    def __init__(self, **args):
        for k,v in args.items():
            setattr(self, k, v)
    
    def _play(self, inst, fn, args, keys):
        """Override this to execute different actions when playing"""
        return fn(args, keys)
    
    def _get(self, name):
        if hasattr(self, 'get_'+name):
            return getattr(self, 'get_'+name)()
        else:
            return getattr(self, name)