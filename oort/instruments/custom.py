from .. import abstract
from .. import utilities
import oort.rtcmix_import as rtcmix

class RISSETBELL(abstract.Instrument):
    instrument="WAVETABLE"
    env = None
    pfields = 'amp', 'pitch', 'pan', 'wavetable'
    def __init__(self, outsk=None, dur=None, AMP=None, PITCH=None, PAN=None, **extra_kwargs):
        self.env = rtcmix.maketable('expbrk', 1000, 1, 1000, 0.0005)
        self._passback(locals())
    
    def get_amp(self):
        return self.amp * 0.2 * self.env
    
    def _play(self, args, keys):
        argdict = dict(zip(keys, args))
        partials  = [ [1., 1., .56, 0, 1.], 
                   [.9, .67, .56, 1., 0.],
                   [.65, 1, .92, 0, 0.9],
                   [.55, 1.8, .92, 1.7, .1],
                   [.325, 2.67, 1.19, 0, .8],
                   [.35, 1.67, 1.7, 0, .2],
                   [.25, 1.46, 2, 0, 0.7],
                   [.2, 1.33, 2.74, 0., 0.3] ]
        
        pan = self._get('pan') * 2 - 1
        if (pan > 0.):
            upperPan = 1.
            lowerPan = (2 - 2 * (1 - pan)) / 2.
        elif (pan < 0.):
            lowerPan = 0.
            upperPan = (2 * (1 + pan)) / 2.
        else:
            lowerPan = 0.
            upperPan = 1.
        for tone in partials:
            pan = utilities.scale_val(tone[4], 0, 1, lowerPan, upperPan)
            argdict['dur'] = self._get('dur') * tone[0]
            argdict['amp'] = self._get('amp') * tone[1]
            argdict['pitch'] = self._get('pitch') * tone[2] + tone[3]
            argdict['pan'] = pan
            args = []
            for argname in keys:
                args.append(argdict[argname])
            
            getattr(rtcmix, self.instrument)(*args)