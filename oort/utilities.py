import rtcmix_import.commands as rtcmix 

def docs(cls):
    return cls().docs()

def scale_val(variable, fromlow, fromhigh, tolow, tohigh):
    amt = (variable - fromlow) / float(fromhigh-fromlow)
    return tolow + amt*(tohigh - tolow)

def mtof(midi):
    return 2. ** ((midi-69) / 12.)*440
    
def ftom(freq):
    import math
    return 12 * math.log((freq/440.), 2)+69

def mtopch(midi):
    octave = int(midi / 12)+3
    hundredths = (midi%12)*.01
    return octave+hundredths

def pchtom(pch):
    octaves = int(pch)-3
    pitch = (pch-int(pch))*100
    return octaves*12+pitch

class Pitch:
    value = None
    fmt = None
    def __init__(self, value, fmt='cps'):
        self.value = value
        self.fmt = fmt
    
    def to_midi(self):
        # Midi will be the default format, because most easily convertable to all others
        if self.fmt in ('cps', 'freq'):
            self.value = ftom(self.value)
        elif self.fmt is 'pch':
            self.value = pchtom(self.value)
        self.fmt = 'midi'
    
    def retrieve(self, fmt='cps'):
        if fmt is self.fmt:
            return self.value
        
        self.to_midi()
        if fmt is 'midi':
            return self.value
        elif fmt is 'pch':
            return mtopch(self.value)
        elif fmt in ('cps', 'freq'):
            return mtof(self.value)

def midi(val):
    return Pitch(val, 'midi')

def pch(val):
    return Pitch(val, 'pch')

def cps(val):
    return Pitch(val, 'cps')

def jointables(*tables):
    """joins any number of tables into a resulting 1000-point table.
    
    Takes any number of arguments.  Each arg can be either a table handle, 
    or a tuple as follows:  (table, scale)
    where scale is the relative size of this table in the sum.
    Otherwise, scale defaults to 1."""
    
    points = []
    
    # we really don't want to log all these samptables:
    printing_was_on = rtcmix.is_print_on
    rtcmix.print_off()
    
    scalesum = 0
    tables_and_scales = []
    for t in tables:
        if type(t) is tuple:
            scale=t[1]
            table=t[0]
        else:
            scale=1
            table=t
        scalesum += scale
        tables_and_scales.append((table, scale))
    
    for table, scale in tables_and_scales:
        allotted_points = int(1000 * scale/float(scalesum))
        tlen = rtcmix.tablelen(table)
        poll_period = tlen/allotted_points
        for i in xrange(allotted_points):
            points.append(rtcmix.samptable(table, i * poll_period))
    #turn printing back on if it was off
    if printing_was_on:
        rtcmix.print_on()
    return rtcmix.maketable('literal', len(points), points)