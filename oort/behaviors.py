import abstract
import schedule
import rtcmix_import as rtcmix


class Jitter(abstract.Behavior):
    """Add degree of random fluctuation to pitch. """
    amt = 0.02
    points = 1000
    required_pfields = 'pitch',
    def __init__(self, amt=0.02, points=1000):
        self.amt=amt
        self.points=points
    
    def get_pitch(self, inst, fn):
        if self.amt <= 0:
            return fn()
        return fn() * (1+rtcmix.maketable('random', 'nonorm', self.points, "even", 1./(1+self.amt)-1, self.amt))

class Humanize(abstract.Behavior):
    """Add random variance to time, pan, amp, and/or pitch."""
    time_variance = 0. # amt of outsk variance in seconds
    pan_variance = 0. # in percentage
    amp_variance = 0. # in decibels
    pitch_variance = 0. # in octaves
    wander=False 
    # if inst vars not reset and wander is true, continue to move randomly away
    # best used with SMALL variances!
    def __init__(self, time_variance=0., pan_variance=0., amp_variance=0., pitch_variance=0., wander=False):
        self.time_variance=time_variance
        self.pan_variance=pan_variance
        self.amp_variance = amp_variance
        self.pitch_variance = pitch_variance
        self.wander = wander
        
    def get_outsk(self, inst, fn):
        import random
        while True:
            variance = random.uniform(-self.time_variance, self.time_variance)
            if schedule.current_time() >= -variance: break
        outsk = fn() + variance
        return outsk
    
    def get_pan(self, inst, fn):
        import random
        pan = fn()
        while True:
            newpan = pan + random.uniform(-self.pan_variance, self.pan_variance)
            if newpan <= 1 and newpan >= 0: break
        if self.wander:
            inst.pan = newpan
        return newpan
    
    def get_amp(self, inst, fn):
        import random
        while True:
            variance = random.uniform(-self.amp_variance, self.amp_variance)
            if variance >= 0: break
        amp = fn() * rtcmix.boost(variance)
        if self.wander:
            inst.amp = amp
        return amp
    
    def get_pitch(self, inst, fn):
        import random
        mult = 2. ** random.uniform(-self.pitch_variance, self.pitch_variance)
        pitch = fn() * mult
        if self.wander:
            inst.pitch = pitch
        return pitch

class ADSR(abstract.Behavior):
    """Apply consistent ADSR envelope to instrument regardless of duration."""
    a=0.1
    d=1
    s=0.5
    r=1
    required_pfields = 'amp',
    def __init__(self, a=0.1, d=1, s=0.5, r=1):
        self.a=a
        self.d=d
        self.s=s
        self.r=r
    
    def get_amp(self, inst, fn):
        points = []
        total_time = 0
        prev_amp = 0
        for time,amp in (0,0), (self.a,1), (self.d,self.s):
            if total_time+time > inst.dur:
                new_time = inst.dur-total_time
                total_time += new_time
                new_amp = prev_amp - (float(prev_amp - amp) * new_time/time)
                time = new_time
                amp = new_amp
                points.append((time, amp))
                break
            total_time += time
            prev_amp = amp
            points.append((time, amp))
        if total_time < inst.dur:
            points.append((inst.dur-total_time,self.s))
        points.append((self.r, 0))
        
        
        args = []
        total_time = 0
        for time,amp in points:
            total_time += time
            args.extend((total_time, amp))
        
        env = rtcmix.maketable('line', 'nonorm', 1000, 0,0, *args)
        return fn() * env
        
    
    def get_dur(self, inst, fn):
        return inst.dur + self.r

class Clickless(ADSR):
    """Apply slight ramps at the edges of note to avoid clicks (especially for wavetable)."""
    a=0.007
    d=0.1
    s=1
    r=0.007
    
    required_pfields = 'amp',
    
    def __init__(self, overlap=0.007):
        self.a=overlap
        self.r=overlap
    
    def _before_play(self, inst, fn, args):
        if inst.min_control_rate < 15000:
            inst.min_control_rate = 15000
        return fn(args)


class Portamento(abstract.Behavior):
    """Slide between the pitches of successive notes."""
    amt = 0.25
    required_pfields = 'pitch',
    def __init__(self, amt=0.25):
        self.amt = amt
        pass
    
    def get_pitch(self, inst, fn):
        target = inst.pitch
        if not hasattr(inst, 'prev_pitch'):
            return fn()

        diff = target - inst.prev_pitch
        dur = inst._get('dur')
        fraction_sliding = float(self.amt)/dur # the fraction of total dur spent sliding
        if fraction_sliding >= 1: # we never actually get there...
            slidetable = rtcmix.maketable('line', 'nonorm', 1000, 0,0, 1, diff / fraction_sliding)
        else:
            slidetable = rtcmix.maketable('line', 'nonorm', 1000, 0,0, fraction_sliding,diff, 1,diff)
        return fn()-diff+slidetable
    
    def _after_play(self, inst, fn, args):
        inst.prev_pitch = inst.pitch
        return fn(args)

class Poly(abstract.Behavior):
    """Plays an instrument {count} number of times each time play() is called.
    Useful in conjunction with other behaviors that involve random elements."""
    count = 10
    def __init__(self, count=10):
        self.count = count
    
    def get_amp(self, inst, fn):
        return fn() / self.count**.8
    
    def _play(self, inst, fn, args, keys):
        #args = list(args)
        for _ in xrange(self.count):
            args, keys = inst.get_instrument_args() #recalc for each
            fn(args, keys)

class Shimmer(Jitter):
    """ Handy combination of Jitter and Poly
    
    The only difference is that here Poly only recalculates pitch each time, allowing
    other randomized parameters to be true to the first randomized parameter."""
    count = 5
    required_pfields = 'pitch',
    def __init__(self, amt=0.02, count=5, points=1000):
        self.amt=amt
        self.count=count
        self.points=points
    
    def get_amp(self, inst, fn):
        return fn() / self.count**.8
    
    def _play(self, inst, fn, args, keys):
        pitch = args[keys.index('pitch')]
        for _ in xrange(self.count):
            args[keys.index('pitch')] = inst.get_pitch()
            fn(args, keys)