import schedule
import rtcmix_import.commands as rtcmix

class Animation(object):
    """An animation is a value that changes over Oort time.
    
    It's value can be polled, or an Animation object can be passed into an instrument
    as a parameter, and the instrument will do the dirty work."""
    
    is_non_negative=None
    def __init__(self, minval=0., maxval=1., dur=10, table=None, loop=False):
        if table is None:
            table = rtcmix.maketable('line',1000, 0,0, 1,1)
        self.min=minval
        self.max=maxval
        self.dur=dur
        self.table=table
        self.start_time=schedule.current_time()
        self.loop=loop
    
    def value(self):
        cur_time = schedule.current_time()
        if cur_time >= self.start_time + self.dur:
            if not self.loop:
                return self.end_val
        
        elapsed = cur_time-self.start_time
        if self.loop:
            elapsed = elapsed%self.dur
        index = float(elapsed)/self.dur*rtcmix.tablelen(self.table)
        val = rtcmix.samptable(self.table, index)
        if self.table_is_non_negative():
            return self.min + (self.max-self.min) * val
        else:
            return self.min + (self.max-self.min) * (val+1.)/2.
    
    def table_is_non_negative(self):
        if self.is_non_negative is None:
            length = rtcmix.tablelen(self.table)
            self.is_non_negative = True
            for x in xrange(50):
                if rtcmix.samptable(self.table, length*x/50.) < 0:
                    self.is_non_negative = False
                    break
        return self.is_non_negative
        
class Ramp(Animation):
    start_val=0.
    end_val=1.
    dur=10
    start_time=None
    def __init__(self, start_val=0., end_val=1., dur=10):
        self.start_time = schedule.current_time()
        self.start_val = start_val
        self.end_val = end_val
        self.dur = dur
    
    def value(self):
        cur_time = schedule.current_time()
        if cur_time < self.start_time:
            return self.start_val
        elif cur_time >= self.start_time + self.dur:
            return self.end_val
        else:
            elapsed = cur_time-self.start_time
            return self.start_val + (self.end_val-self.start_val) * (float(elapsed) / self.dur)
