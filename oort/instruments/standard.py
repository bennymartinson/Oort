from ..abstract import Instrument, Effect
from .. import rtcmix_import as rtcmix

""" INSTRUMENTS """
class AMINST(Instrument):
    """AMINST(outsk, dur, AMP, CARFREQ (Hz), MODFREQ (Hz)[, PAN, MODAMPENV, CARWAVETABLE, MODWAVETABLE])"""
    instrument = "AMINST"
    pfields = 'amp','carfreq','modfreq','pan','modampenv','carwavetable','modwavetable'
    def __init__(self, outsk=None, dur=None, amp=None, carfreq=None, modfreq=None, pan=None, modampenv=None, carwavetable=None, modwavetable=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class CLAR(Instrument):
    """CLAR(outsk, dur, noiseamp, length1 (samples), length2 (samples), outputamp, d2gain[, pan])"""
    instrument = "CLAR"
    pfields = (),
    noiseamp = 0.02
    length1 = 78
    length2 = 31
    d2gain = 0
    def __init__(self, outsk=None, dur=None, noiseamp=None, length1=None, length2=None, amp=None, d2gain=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class DUMP(Instrument):
    """DUMP(outsk, dur, AMP[, TABLE])"""
    instrument = "DUMP"
    pfields = 'amp', 'table'
    def __init__(self, outsk=None, dur=None, amp=None, table=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class FMINST(Instrument):
    """FMINST(outsk, dur, AMP, CARFREQ (Hz/oct.pc), MODFREQ (Hz/oct.pc), LOWINDEX, HIGHINDEX[, PAN, WAVETABLE, INDEXENV])"""
    instrument = "FMINST"
    pfields = 'amp', 'carfreq', 'modfreq', 'lowindex', 'highindex', 'pan', 'wavetable', 'indexenv'
    def __init__(self, outsk=None, dur=None, amp=None, carfreq=None, modfreq=None, lowindex=None, highindex=None, pan=None, wavetable=None, indexenv=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class GRANSYNTH(Instrument):
    """GRANSYNTH(outsk, dur, AMP, WAVETABLE, GRAINENV, GRAINHOP, OUTTIMEJITTER, MINDUR, MAXDUR, MINAMP, MAXAMP, PITCH[, TRANSPTABLE, PITCHJITTER, seed, MI
, MAXPAN])"""
    instrument = "GRANSYNTH"
    pfields = 'amp', 'wavetable', 'grainenv', 'grainhop', 'outtimejitter', 'mindur', 'maxdur', 'minamp', 'maxamp', 'pitch', 'transptable', 'pitchjitter', 'minpan', 'maxpan'
    def __init__(self, outsk=None, dur=None, amp=None, wavetable=None, grainenv=None, grainhop=None, outtimejitter=None, mindur=None, maxdur=None, minamp=None, maxamp=None, pitch=None, transtable=None, pitchjitter=None, seed=None, minpan=None, maxpan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class HALFWAVE(Instrument):
    """HALFWAVE(outsk, dur, PITCH, AMP, FIRSTHALF, SECONDHALF, WMIDPOINT[, PAN])"""
    instrument = "HALFWAVE"
    pfields = 'pitch', 'amp', 'firsthalf', 'secondhalf', 'wmidpoint', 'pan'
    def __init__(self, outsk=None, dur=None, pitch=None, amp=None, firsthalf=None, secondhalf=None, wmidpoint=None, pan=None):
        self._passback(locals())
class JGRAN(Instrument):
    """JGRAN(outsk, dur, AMP, seed, osctype, phaserandom, GRAINENV, GRAINWAVE, MODFREQMULT, MODINDEX, MINFREQ, MAXFREQ, MINSPEED, MAXSPEED, MININTENSITY, MAXINTENSITY, DENSITY[, PAN, PANRANDOM])"""
    instrument = "JGRAN"
    pfields= 'amp', 'grainenv', 'grainwave', 'modfreqmult', 'modindex', 'minfreq', 'maxfreq', 'minspeed', 'maxspeed', 'minintensity', 'maxintensity', 'destiny', 'pan', 'panrandom'
    def __init__(self, outsk=None, dur=None, amp=None, seed=None, osctype=None, phaserandom=None, grainenv=None, grainwave=None, modfreqmult=None, modindex=None, minfreq=None, maxfreq=None, minspeed=None, maxspeed=None, minintensity=None, maxintensity=None, density=None, pan=None, panrandom=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class LPCPLAY(Instrument):
    """LPCPLAY(outsk, dur, AMP, PITCH, startframe, endframe[, WARP, RESONCF, RESONBW])"""
    instrument = "LPCPLAY"
    pfields = 'amp', 'pitch', 'warp', 'resoncf', 'resonbw'
    def __init__(self, outsk=None, dur=None, amp=None, pitch=None, startframe=None, endframe=None, warp=None, resoncf=None, resonbw=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class BUZZ(Instrument):
    """BUZZ(outsk, dur, AMP, PITCH (Hz/oct.pc)[, PAN])"""
    instrument = "BUZZ"
    load = "IIR"
    pfields = 'amp', 'pitch', 'pan'
    def __init__(self, outsk=None, dur=None, amp=None, pitch=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class PULSE(Instrument):
    """PULSE(outsk, dur, AMP, PITCH (Hz/oct.pc)[, PAN])"""
    instrument = "PULSE"
    load = "IIR"
    pfields = 'amp', 'pitch', 'pan'
    def __init__(self, outsk=None, dur=None, amp=None, pitch=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MBANDEDWG(Instrument):
    """MBANDEDWG(outsk, dur, amp, pitch, strikepos, pluckflag, maxvel, preset, bowpressure, resonance, integration[, pan {default: 0.5}, velocityenv])"""
    instrument = "MBANDEDWG"
    strikepos = 0.5
    pluckflag = 1
    maxvel = 1
    preset = 0
    bowpressure = 0.
    resonance = 0.99
    integration = 0.
    velocityenv = None
    pfields = 'amp', 'pitch', 'bowpressure', 'resonance', 'integration', 'pan', 'velocityenv'
    def __init__(self, outsk=None, dur=None, amp=None, pitch=None, strikepos=None, pluckflag=None, maxvel=None, preset=None, bowpressure=None, resonance=None, integration=None, pan=None, velocityenv=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MBLOWBOTL(Instrument):
    """MBLOWBOTL(outsk, dur, amp, pitch, noiseamp, maxpressure[, pan {default: 0.5}, pressureenv])"""
    instrument = "MBLOWBOTL"
    pfields = 'amp', 'pitch', 'noiseamp', 'pan', 'pressureenv'
    def __init__(self, outsk=None, dur=None, amp=None, pitch=None, noiseamp=None, maxpressure=None, pan=None, pressureenv=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MBLOWHOLE(Instrument):
    """MBLOWHOLE(outsk, dur, amp, pitch, noiseamp, maxpressure, reedstiff, tonehole, vent[, pan {default: 0.5}, pressureenv])"""
    instrument = "MBLOWHOLE"
    pfields = 'amp', 'freq', 'noiseamp', 'reedstiff', 'tonehole', 'vent', 'pan', 'pressureenv'
    def __init__(self, outsk=None, dur=None, amp=None, pitch=None, noiseamp=None, maxpressure=None, reedstiff=None, tonehole=None, vent=None, pan=None, pressureenv=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MBOWED(Instrument):
    """MBOWED(outsk, dur, amp, pitch, vibfreqlo, vibfreqhi, vibdepth[, pan {default: 0.5}, bowvelenv, bowpressenv, bowposenv, vibtable])"""
    instrument = "MBOWED"
    pfields = 'amp', 'freq', 'vibdepth', 'pan', 'bowvelenv', 'bowpressenv', 'bowposenv', 'vibtable'
    vibfreqlo=5
    vibfreqhi=7
    vibdepth=0.02
    def __init__(self, outsk=None, dur=None, amp=None, pitch=None, vibfreqlo=None, vibfreqhi=None, vibdepth=None, pan=None, bowvelenv=None, bowpressenv=None, bowposenv=None, vibtable=None, *extra_args, **extra_kwargs):
        self.bowvelenv = rtcmix.maketable('line', 1000, 0,0, 1,1, 2,0)
        self.bowpressenv = rtcmix.maketable('line', 1000, 0,1, 1,1)
        self.bowposenv = rtcmix.maketable('line', 1000, 0,1, 2,0, 3,1)
        self.vibtable = rtcmix.maketable('wave', 1000, 'sine')
        self._passback(locals())
class MBRASS(Instrument):
    """MBRASS(outsk, dur, amp, pitch, slidelen, lipfilt, maxpressure[, pan {default: 0.5}, breathenv])"""
    instrument = "MBRASS"
    pfields = 'amp', 'freq', 'slidelen', 'lipfilt', 'pan', 'breathenv'
    def __init__(self, outsk=None, dur=None, amp=None, pitch=None, slidelen=None, lipfilt=None, maxpressure=None, pan=None, breathenv=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MCLAR(Instrument):
    """MCLAR(outsk, dur, amp, pitch, noiseamp, maxpressure, reedstiff[, pan {default: 0.5}, breathenv])"""
    instrument = "MCLAR"
    pfields = 'amp', 'freq', 'noiseamp', 'reedstuff', 'pan', 'breathenv'
    def __init__(self, outsk=None, dur=None, amp=None, pitch=None, noiseamp=None, maxpressure=None, reedstuff=None, pan=None, breathenv=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class SFLUTE(Instrument):
    """SFLUTE(outskip, dur, noiseamp, length1 (samples), length2 (samples), amp[, pan])"""
    instrument = "SFLUTE"
    load = "METAFLUTE"
    def __init__(self, outskip=None, dur=None, noiseamp=None, length1=None, length2=None, amp=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class VSFLUTE(Instrument):
    """VSFLUTE(outskip, dur, noiseamp, length1low (samples), length1high (samples), length2low (samples), length2high (samples), amp, vibfreq1low (Hz), vibfreq1high (Hz), vibfreq2low (Hz), vibfreq2high (Hz)[, pan])"""
    instrument = "VSFLUTE"
    load = "METAFLUTE"
    def __init__(self, outskip=None, dur=None, noiseamp=None, length1low=None, length1high=None, length2low=None, length2high=None, amp=None, vibfreq1low=None, vibfreq1high=None, vibfreq2low=None, vibfreq2high=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class BSFLUTE(Instrument):
    """BSFLUTE(outskip, dur, noiseamp, length1low (samples), length1high (samples), length2low (samples), length2high (samples), amp[, pan])"""
    instrument = "BSFLUTE"
    load = "METAFLUTE"
    def __init__(self, outskip=None, dur=None, noiseamp=None, length1low=None, length1high=None, length2low=None, length2high=None, amp=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class LSFLUTE(Instrument):
    """LSFLUTE(outskip, dur, noiseamp, length1 (samples), length2 (samples), amp[, pan])"""
    instrument = "LSFLUTE"
    load = "METAFLUTE"
    def __init__(self, outskip=None, dur=None, noiseamp=None, length1=None, length2=None, amp=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())

class MMESH2D(Instrument):
    """MMESH2D(outsk, dur, amp, nxpoints, nypoints, xpos, ypos, decay, strike[, pan {default: 0.5}])"""
    instrument = "MMESH2D"
    pfields = 'amp', 'pan'
    def __init__(self, outsk=None, dur=None, amp=None, nxpoints=None, nypoints=None, xpos=None, ypos=None, decay=None, strike=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MMODALBAR(Instrument):
    """MMODALBAR(outsk, dur, amp, pitch, hardness, pos, preset[, pan {default: 0.5}, ampenv])"""
    instrument = "MMODALBAR"
    pfields = 'amp', 'freq', 'pan', 'ampenv'
    def __init__(self, outsk=None, dur=None, amp=None, pitch=None, hardness=None, pos=None, preset=None, pan=None, ampenv=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MSAXOFONY(Instrument):
    """MSAXOFONY(outsk, dur, amp, pitch, noiseamp, maxpressure, reedstiff, aperture, blowpos[, pan {default: 0.5}, breathenv])"""
    instrument = "MSAXOFONY"
    pfields = 'amp', 'freq', 'noiseamp', 'reedstuff', 'aperture', 'blowpos', 'pan', 'breathenv'
    def __init__(self, outsk=None, dur=None, amp=None, pitch=None, noiseamp=None, maxpressure=None, reedstuff=None, aperture=None, blowpos=None, pan=None, breathenv=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MSHAKERS(Instrument):
    """MSHAKERS(outsk, dur, amp, energy, decay, nobjs, resonance, instrument[, pan {default: 0.5}])"""
    instrument = "MSHAKERS"
    pfields = 'amp', 'energy', 'decay', 'nobjs', 'resonance', 'pan'
    def __init__(self, outsk=None, dur=None, amp=None, energy=None, decay=None, nobjs=None, resonance=None, instrument=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MSITAR(Instrument):
    """MSITAR(outsk, dur, amp, pitch, plamp[, pan {default: 0.5}, ampenv])"""
    instrument = "MSITAR"
    pfields = 'amp', 'freq', 'pan', 'ampenv'
    def __init__(self, outsk=None, dur=None, amp=None, pitch=None, plamp=None, pan=None, ampenv=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MULTIWAVE(Instrument):
    """MULTIWAVE(outsk, dur, AMP, WAVETABLE, FREQ1, AMP1, phase1, PAN1, ... FREQN, AMPN, phaseN, PANN)"""
    instrument = "MULTIWAVE"
    pfields = 'amp', 'wavetable'
    kw_pattern = 'freq', 'amp', 'phase', 'pan'
    def __init__(self, outsk=None, dur=None, amp=None, wavetable=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class NOISE(Instrument):
    """NOISE(outsk, dur, AMP[, PAN])"""
    instrument = "NOISE"
    pfields = 'amp', 'pan'
    def __init__(self, outsk=None, dur=None, amp=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class SCULPT(Instrument):
    """SCULPT(outsk, segmentdur, amp, nsegments[, pan])"""
    instrument = "SCULPT"
    pfields = ()
    def __init__(self, outsk=None, segmentdur=None, amp=None, nsegments=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class SGRANR(Instrument):
    """SGRANR(outsk, dur, amp, rate, p4-7: ratevar, p8-11: duration, p12-15: location, p16-19: transposition[, grainlayers (not used), seed])"""
    instrument = "SGRANR"
    pfields = ()
    def __init__(self, outsk=None, dur=None, amp=None, rate=None, *extra_args, **extra_kwargs):
        self._passback(locals()) 
class SYNC(Instrument):
    """SYNC(outsk, dur, PITCH, AMP, OSCFREQ, OSCWAVE[, PAN])"""
    instrument = "SYNC"
    pfields = 'pitch', 'amp', 'oscfreq', 'oscwave', 'pan'
    def __init__(self, outsk=None, dur=None, pitch=None, amp=None, oscfreq=None, oscwave=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals()) 
class START(Instrument):
    funddecay=1.
    nyqdecay=0.1
    squish=1
    """START(outsk, dur, pitch, funddecay, nyqdecay, amp, squish[, pan, deleteflag])"""
    instrument = "START"
    load = "STRUM"
    def __init__(self, outsk=None, dur=None, pitch=None, funddecay=None, nyqdecay=None, amp=None, squish=None, pan=None, deleteflag=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class BEND(Instrument):
    """BEND(outsk, dur, pitch0, pitch1, glissfunc, funddecay, nyqdecay[, updaterate, pan])"""
    instrument = "BEND"
    load = "STRUM"
    def __init__(self, outsk=None, dur=None, pitch0=None, pitch1=None, glissfunc=None, funddecay=None, nyqdecay=None, updaterate=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class FRET(Instrument):
    """FRET(outsk, dur, pitch, funddecay, nyqdecay[, pan])"""
    instrument = "FRET"
    load = "STRUM"
    def __init__(self, outsk=None, dur=None, pitch=None, funddecay=None, nyqdecay=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class START1(Instrument):
    """START1(outsk, dur, pitch, funddecay, nyqdecay, distortiongain, feedbackgain, feedbackpitch, cleanlevel, distortionlevel, amp, squish [, pan, deleteflag])"""
    instrument = "START1"
    load = "STRUM"
    def __init__(self, outsk=None, dur=None, pitch=None, funddecay=None, nyqdecay=None, distortiongain=None, feedbackgain=None, feedbackpitch=None, cleanlevel=None, distortionlevel=None, amp=None, squish=None, pan=None, deleteflag=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class BEND1(Instrument):
    """BEND1(outsk, dur, pitch0, pitch1, glissfunc, funddecay, nyqdecay, distortiongain, feedbackgain, feedbackpitch, cleanlevel, distortionlevel, amp, updatefreq[, pan])"""
    instrument = "BEND1"
    load = "STRUM"
    def __init__(self, outsk=None, dur=None, pitch0=None, pitch1=None, glissfunc=None, funddecay=None, nyqdecay=None, distortiongain=None, feedbackgain=None, feedbackpitch=None, cleanlevel=None, distortionlevel=None, amp=None, updatefreq=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class FRET1(Instrument):
    """FRET1(outsk, dur, pitch, funddecay, nyqdecay, distortiongain, feedbackgain, feedbackpitch, cleanlevel, distortionlevel, amp[, pan])"""
    instrument = "FRET1"
    load = "STRUM"
    def __init__(self, outsk=None, dur=None, pitch=None, funddecay=None, nyqdecay=None, distortiongain=None, feedbackgain=None, feedbackpitch=None, cleanlevel=None, distortionlevel=None, amp=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class VSTART1(Instrument):
    """VSTART1(outsk, dur, pitch, funddecay, nyqdecay, distortiongain, feedbackgain, feedbackpitch, cleanlevel, distortionlevel, amp, squish, lowvibrato, hivibrato, vibratodepth[, randomseed, updaterate, pan, deleteflag])"""
    instrument = "VSTART1"
    load = "STRUM"
    def __init__(self, outsk=None, dur=None, pitch=None, funddecay=None, nyqdecay=None, distortiongain=None, feedbackgain=None, feedbackpitch=None, cleanlevel=None, distortionlevel=None, amp=None, squish=None, lowvibrato=None, hivibrato=None, vibratodepth=None, randomseed=None, updaterate=None, pan=None, deleteflag=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class VFRET1(Instrument):
    """VFRET1(outsk, dur, pitch, funddecay, nyqdecay, distortiongain, feedbackgain, feedbackpitch, cleanlevel, distortionlevel, amp, lowvibrato, hivibrato, vibratodepth[, updaterate, pan])"""
    instrument = "VFRET1"
    load = "STRUM"
    def __init__(self, outsk=None, dur=None, pitch=None, funddecay=None, nyqdecay=None, distortiongain=None, feedbackgain=None, feedbackpitch=None, cleanlevel=None, distortionlevel=None, amp=None, lowvibrato=None, hivibrato=None, vibratodepth=None, updaterate=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class STRUM2(Instrument):
    """STRUM2(outsk, dur, AMP, PITCH, squish, decay_time[, PAN])"""
    instrument = "STRUM2"
    def __init__(self, outsk=None, dur=None, AMP=None, PITCH=None, squish=None, decay_time=None, PAN=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class STRUMFB(Instrument):
    """STRUMFB(outsk, dur, AMP, PITCH, FEEDBACK_PITCH, squish, FUND_DECAY, NYQ_DECAY, DISTORTION_GAIN, FEEDBACK_GAIN, CLEANLEVEL, DISTLEVEL[, PAN])"""
    instrument = "STRUMFB"
    def __init__(self, outsk=None, dur=None, AMP=None, PITCH=None, FEEDBACK_PITCH=None, squish=None, FUND_DECAY=None, NYQ_DECAY=None, DISTORTION_GAIN=None, FEEDBACK_GAIN=None, CLEANLEVEL=None, DISTLEVEL=None, PAN=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class WAVETABLE(Instrument):
    """WAVETABLE(outsk, dur, AMP, PITCH[, PAN, WAVETABLE])"""
    instrument = "WAVETABLE"
    pfields = 'amp', 'pitch', 'pan', 'wavetable'
    def __init__(self, outsk=None, dur=None, amp=None, pitch=None, pan=None, wavetable=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class WAVESHAPE(Instrument):
    """WAVESHAPE(outsk, dur, PITCH, INDEXMIN, INDEXMAX, AMP, PAN, WAVETABLE, TRANSFERFUNCTION, INDEXENV[, ampnormalize])"""
    instrument = "WAVESHAPE"
    pfields = 'pitch', 'indexmin', 'indexmax', 'amp', 'pan', 'wavetable', 'transferfunction', 'indexenv'
    def __init__(self, outsk=None, dur=None, pitch=None, indexmin=None, indexmax=None, amp=None, pan=None, wavetable=None, transferfunction=None, indexenv=None, ampnormalize=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class WAVY(Instrument):
    """WAVY(outsk, dur, amp, freqA (Hz/oct.pc), freqB (Hz/oct.pc), phaseB (0-1), wavetableA, wavetableB, expr, pan)"""
    instrument = "WAVY"
    pfields = 'amp', 'freqa', 'freqb', 'phaseb', 'wavetablea', 'wavetableb', 'pan'
    def __init__(self, outsk=None, dur=None, amp=None, freqa=None, freqb=None, phaseb=None, wavetablea=None, wavetableb=None, expr=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class WIGGLE(Instrument):
    """WIGGLE(outsk, dur, caramp, carfreq (Hz/oct.pc)[, moddepthtype, filttype, steepness {default: 1}, balance, carwave, modwave, modfreq, moddepth, lowpassfreq, pan])"""
    instrument = "WIGGLE"
    pfields = 'caramp', 'carfreq', 'carwave', 'modwave', 'modfreq', 'moddepth', 'lowpassfreq', 'pan'
    def __init__(self, outsk=None, dur=None, caramp=None, carfreq=None, moddepthcontrol=None, filttype=None, steepness=None, balance=None, carwave=None, modwave=None, modfreq=None, moddepth=None, lowpassfreq=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())

""" EFFECTS """
class AM(Effect):
    """AM(outsk, insk, dur, AMP, MODFREQ (hz)[, inputchan, PAN, MODWAVETABLE])"""
    instrument = "AM"
    pfields = 'amp', 'modfreq', 'pan', 'modwavetable'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, modfreq=None, inputchan=None, pan=None, modwavetable=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class BUTTER(Effect):
    """BUTTER(outsk, insk, dur, AMP, FILTTYPE, steepness, ampbalance, inputchan, PAN, BYPASS, FREQENV[, BANDWIDTH])"""
    instrument = "BUTTER"
    pfields = 'amp', 'filttype', 'pan', 'bypass', 'freqenv', 'bandwidth'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, filttype=None, steepness=None, ampbalance=None, inputchan=None, pan=None, bypass=None, freqenv=None, bandwidth=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class COMBIT(Effect):
    """COMBIT(outsk, insk, dur, AMP, FREQ (Hz), REVERBTIME[, inputchan, PAN, ringdowndur])"""
    instrument = "COMBIT"
    pfields = 'amp','freq','reverbtime','pan'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, pitch=None, reverbtime=None, inputchan=None, pan=None, ringdowndur=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class COMPLIMIT(Effect):
    """COMPLIMIT(outsk, insk, dur, PREAMP, POSTAMP, ATTACK, RELEASE, THRESHOLD, COMPRESSRATIO, lookahead, windowsize[, DETECTIONTYPE, BYPASS, INPUTCHAN, PAN])"""
    instrument = "COMPLIMIT"
    pfields = 'preamp','postamp','attack','release', 'threshold', 'compressratio', 'detectiontype', 'bypass', 'inputchan', 'pan'
    def __init__(self, outsk=None, insk=None, dur=None, preamp=None, postamp=None, attack=None, release=None, threshold=None, compressratio=None, lookahead=None, windowsize=None, detectiontype=None, bypass=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class CONVOLVE1(Effect):
    """CONVOLVE1(outsk, insk, dur, AMP, IMPULSETABLE, impstart, impudur, impamp, WINDOWTABLE, AMTWET, inputchan, PAN)"""
    instrument = "CONVOLVE1"
    pfields = 'amp', 'impulsetable', 'windowtable', 'amtwet', 'pan'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, impulsetable=None, impstart=None, impudur=None, impamp=None, windowtable=None, amtwet=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class DCBLOCK(Effect):
    """DCBLOCK(outsk, insk, dur, AMP)"""
    instrument = "DCBLOCK"
    pfields = 'amp'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class DECIMATE(Effect):
    """DECIMATE(outsk, insk, dur, PREAMP, POSTAMP, NBITS[, LOWPASSFREQ, inputchan, PAN])"""
    instrument = "DECIMATE"
    pfields = 'preamp', 'postamp', 'nbits', 'lowpassfreq', 'pan'
    def __init__(self, outsk=None, insk=None, dur=None, preamp=None, postamp=None, nbits=None, lowpassfreq=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class DEL1(Effect):
    """DEL1(outsk, insk, dur, AMP, DELAYTIME, DELAYAMP[, inputchan, ringdowndur])"""
    instrument = "DEL1"
    pfields = 'amp', 'delaytime', 'delayamp'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, delaytime=None, delayamp=None, inputchan=None, ringdowndur=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class DELAY(Effect):
    """DELAY(outsk, insk, indur, AMP, DELAYTIME, FEEDBACK, ringdowndur[, inputchan, PAN])"""
    instrument = "DELAY"
    pfields = 'amp', 'delaytime', 'feedback', 'pan'
    def __init__(self, outsk=None, insk=None, indur=None, amp=None, delaytime=None, feedback=None, ringdowndur=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class DISTORT(Effect):
    """DISTORT(outsk, insk, dur, AMP, disttype, PREAMP, LOWPASSFREQ[, inputchan, PAN, BYPASS])"""
    instrument = "DISTORT"
    pfields = 'amp', 'preamp', 'lowpassfreq', 'pan', 'bypass'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, disttype=None, preamp=None, lowpassfreq=None, inputchan=None, pan=None, bypass=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class DMOVE(Effect):
    """DMOVE(outsk, insk, dur, AMP, DIST-XPOS, ANGLE-YPOS, (-)dist_mikes[, inchan])"""
    instrument = "DMOVE"
    pfields = 'amp', 'dist_xpos', 'angle_ypos'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, dist_xpos=None, angle_ypos=None, dist_mikes=None, inchan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class RVB(Effect):
    """RVB(outsk, insk, dur, AMP)"""
    instrument = "RVB"
    def __init__(self, outsk=None, insk=None, dur=None, AMP=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class ELL(Effect):
    """ELL(outsk, insk, dur, AMP, ringdowndur[, inputchan, PAN])"""
    instrument = "ELL"
    pfields = 'amp', 'eqtype', 'pan', 'bypass', 'filtfreq', 'filtq', 'filtamp'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, eqtype=None, inputchan=None, pan=None, bypass=None, filtfreq=None, filtq=None, filtamp=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class EQ(Effect):
    """EQ(outsk, insk, dur, AMP, EQTYPE, inputchan, PAN, BYPASS, FILTFREQ, FILTQ[, FILTAMP])"""
    instrument = "EQ"
    pfields = 'amp', 'eqtype', 'pan', 'bypass', 'filtfreq', 'filtq', 'filtamp'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, eqtype=None, inputchan=None, pan=None, bypass=None, filtfreq=None, filtq=None, filtamp=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class FILTERBANK(Effect):
    """FILTERBANK(outsk, insk, dur, AMP, ringdowndur, inputchan, PAN, CFREQ1, BANDWIDTH1, RELAMP1, ... CFREQN, BANDWITHN, RELAMPN)"""
    instrument = "FILTERBANK"
    pfields = 'amp', 'pan'
    kw_pattern = 'cfreq', 'bandwidth', 'relamp'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, ringdowndur=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class FILTSWEEP(Effect):
    """FILTSWEEP(outsk, insk, dur, AMP, ringdowndur, steepness, ampbalance, inputchan, PAN, BYPASS, CENTERFREQENV, BANDWIDTHENV)"""
    instrument = "FILTSWEEP"
    pfields = 'amp', 'pan', 'bypass', 'centerfreqenv', 'bandwidthenv'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, ringdowndur=None, steepness=None, ampbalance=None, inputchan=None, pan=None, bypass=None, centerfreqenv=None, bandwidthenv=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class FIR(Effect):
    """FIR(outsk, insk, dur, AMP, ncoefficients, coefficients...)"""
    instrument = "FIR"
    pfields = 'amp'
    kw_pattern = 'coefficient'
    def __init__(self, outsk=None, insk=None, amp=None, ncoefficients=None):
        self._passback(locals())
class FLANGE(Effect):
    """FLANGE(outsk, insk, dur, AMP, RESONANCE, maxdelay, MODDEPTH, MODRATE, SIGNALMIX[, FLANGETYPE, inputchan, PAN, ringdowndur, MODWAVETABLE])"""
    instrument = "FLANGE"
    pfields = 'amp', 'resonance', 'moddepth', 'modrate', 'signalmix', 'flangetype', 'pan', 'modwavetable'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, resonance=None, maxdelay=None, moddepth=None, modrate=None, signalmix=None, flangetype=None, inputchan=None, pan=None, ringdowndur=None, modwavetable=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class FOLLOWBUTTER(Effect):
    """FOLLOWBUTTER(outsk, insk, dur, CARAMP, MODAMP, windowsize, SMOOTHNESS, FILTTYPE, MINFREQ, MAXFREQ, steepness, PAN[, BANDWIDTH])"""
    instrument = "FOLLOWBUTTER"
    pfields = 'caramp', 'modamp', 'smoothness', 'filttype', 'minfreq', 'maxfreq', 'pan', 'bandwidth'
    def __init__(self, outsk=None, insk=None, dur=None, caramp=None, modamp=None, windowsize=None, smoothness=None, filttype=None, minfreq=None, maxfreq=None, steepness=None, pan=None, bandwidth=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class FOLLOWER(Effect):
    """FOLLOWER(outsk, insk, dur, CARAMP, MODAMP, windowsize, SMOOTHNESS[, PAN])"""
    instrument = "FOLLOWER"
    pfields = 'caramp', 'modamp', 'smoothness', 'pan'
    def __init__(self, outsk=None, insk=None, dur=None, caramp=None, modamp=None, windowsize=None, smoothness=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class FOLLOWGATE(Effect):
    """FOLLOWGATE(outsk, insk, dur, CARAMP, MODAMP, windowsize, SMOOTHNESS, ATTACK, RELEASE, PAN, POWERTHRESHOLDTABLE, RANGETABLE)"""
    instrument = "FOLLOWGATE"
    pfields = 'caramp', 'modamp', 'smoothness', 'attack', 'release', 'pan', 'powerthresholdtable', 'rangetable'
    def __init__(self, outsk=None, insk=None, dur=None, caramp=None, modamp=None, windowsize=None, smoothness=None, attack=None, release=None, pan=None, powerthresholdtable=None, rangetable=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class FREEVERB(Effect):
    """FREEVERB(outsk, insk, dur, AMP, ROOMSIZE, PREDELAY, ringdowndur, DAMP, DRYSIG, WETSIG, STEREOWIDTH)"""
    instrument = "FREEVERB"
    pfields = 'amp', 'roomsize', 'predelay', 'damp', 'drysig', 'wetsig', 'stereowidth'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, roomsize=None, predelay=None, ringdowndur=None, damp=None, drysig=None, wetsig=None, stereowidth=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class GRANULATE(Effect):
    """GRANULATE(outsk, INSK, dur, AMP, INPUTTABLE, inchans, INTABLECHAN, INSTART, INEND, WRAPAROUND, TRAVERSERATE, GRAINENV, GRAINHOP, INTIMEJITTER, OUTTIMEJITTER, MINDUR, MAXDUR, MINAMP, MAXAMP, PITCH[, TRANSPTABLE, PITCHJITTER, seed, MINPAN, MAXPAN, INTERPTYPE])"""
    instrument = "GRANULATE"
    pfields = 'insk', 'amp', 'inputtable', 'intablechan', 'instart', 'inend', 'wraparound', 'traverserate', 'grainenv', 'grainhop', 'intimejitter', 'outtimejitter', 'mindur', 'maxdur', 'minamp', 'maxamp', 'pitch', 'transptable', 'pitchjitter', 'minpan', 'maxpan', 'interptype'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, inputtable=None, inchans=None, intablechan=None, instart=None, inend=None, wraparound=None, traverserate=None, grainenv=None, grainhop=None, intimejitter=None, outtimejitter=None, mindur=None, maxdur=None, minamp=None, maxamp=None, pitch=None, transptable=None, pitchjitter=None, seed=None, minpan=None, maxpan=None, interptype=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class GVERB(Effect):
    """GVERB(outsk, insk, dur, AMP, ROOMSIZE, RVBTIME, DAMPING, BANDWIDTH, DRYLEVEL, EARLYREFLECT, RVBTAIL, RINGDOWN[, INCHAN])"""
    instrument = "GVERB"
    pfields = 'amp', 'roomsize', 'rvbtime', 'damping', 'bandwidth', 'drylevel', 'earlyreflect', 'rvbtail', 'ringdown', 'inchan'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, roomsize=None, rvbtime=None, damping=None, bandwidth=None, drylevel=None, earlyreflect=None, rvbtail=None, ringdown=None, inchan=None):
        self._passback(locals())
class HOLO(Effect):
    """HOLO(outsk, insk, dur, AMP, XTALKMULT)"""
    instrument = "HOLO"
    pfields = 'amp', 'xtalkmult'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, xtalkmult=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class INPUTSIG(Effect):
    """INPUTSIG(outsk, insk, dur, AMP[, inputchan, PAN])"""
    instrument = "INPUTSIG"
    pfields = 'amp', 'pan'
    def __init__(self, outsk=None, insk=None, dur=None, AMP=None, inputchan=None, PAN=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class JCHOR(Effect):
    """JCHOR(outsk, insk, dur, indur, inmaintain, pitch, nvoices, MINAMP, MAXAMP, MINWAIT, MAXWAIT, seed, inputchan, AMPENV, GRAINENV)"""
    instrument = "JCHOR"
    pfields = 'minamp', 'maxamp', 'minwait', 'maxwait', 'ampenv', 'grainenv'
    def __init__(self, outsk=None, insk=None, dur=None, indur=None, inmaintain=None, pitch=None, nvoices=None, minamp=None, maxamp=None, minwait=None, maxwait=None, seed=None, inputchan=None, ampenv=None, grainenv=None, *extra_args, **extra_kwargs):
        self._passback(locals()) 
class JDELAY(Effect):
    """JDELAY(outsk, insk, dur, AMP, DELAYTIME, FEEDBACK, ringdowndur, FILTFREQ, SIGMIX[, inputchan, PAN, prefadesend, dcblock])"""
    instrument = "JDELAY"
    pfields = 'amp', 'delaytime', 'feedback', 'filtfreq', 'sigmix', 'pan'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, delaytime=None, feedback=None, ringdowndur=None, filtfreq=None, sigmix=None, inputchan=None, pan=None, prefadesend=None, dcblock=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class JFIR(Effect):
    """JFIR(outsk, insk, dur, AMP, filtorder, inputchan, PAN, BYPASS, FREQTABLE)"""
    instrument = "JFIR"
    pfields = 'amp', 'pan', 'bypass', 'freqtable'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, filtorder=None, inputchan=None, pan=None, bypass=None, freqtable=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class LPCIN(Effect):
    """LPCIN(outsk, insk, dur, AMP, startframe, endframe[, WARP, RESONCF, RESONBW])"""
    instrument = "LPCIN"
    def __init__(self, outsk=None, insk=None, dur=None, AMP=None, startframe=None, endframe=None, WARP=None, RESONCF=None, RESONBW=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MIX(Effect):
    """MIX(outsk, insk, dur, AMP, p4-n: output channel assigns)"""
    instrument = "MIX"
    pfields = 'amp',
    load = ()
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, *extra_args, **extra_kwargs):
        self._passback(locals())

class MMOVE(Effect):
    """MMOVE(outskip, inskip, dur, AMP, dist_between_mikes[, inputchan])"""
    instrument = "MMOVE"
    def __init__(self, outskip=None, inskip=None, dur=None, AMP=None, dist_between_mikes=None, inputchan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MPLACE(Effect):
    """MPLACE(outskip, inskip, dur, AMP, dist-xpos, angle-ypos, (-)dist_mikes[, input_channel])"""
    instrument = "MPLACE"
    pfields = 'amp',
    def __init__(self, outskip=None, inskip=None, dur=None, amp=None, dist_between_mikes=None, inputchan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MOCKBEND(Effect):
    """MOCKBEND(outsk, insk, dur, amp, pitchenvgenno[, inputchan, pan])"""
    instrument = "MOCKBEND"
    pfields = ()
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, pitchenvgenno=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MOOGVCF(Effect):
    """MOOGVCF(outsk, insk, dur, AMP, inputchan, PAN, BYPASS, FILTFREQTABLE, FILTRESONTABLE)"""
    instrument = "MOOGVCF"
    pfields = 'amp', 'pan', 'bypass', 'filtfreqtable', 'filtresontable'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, inputchan=None, pan=None, bypass=None, filtfreqtable=None, filtresontable=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MOVE(Effect):
    """MOVE(outskip, inskip, dur, AMP, dist_between_mikes, rvb_amp[, inputchan])"""
    instrument = "MOVE"
    pfields = 'amp',
    def __init__(self, outskip=None, inskip=None, dur=None, amp=None, dist_between_mikes=None, rvb_amp=None, inputchan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MROOM(Effect):
    """MROOM(outsk, insk, dur, amp, rightdist, frontdist, rvbtime, reflect, inroomwidth[, inputchan, updaterate {default: resetval}])"""
    instrument = "MROOM"
    pfields = ()
    def __init__(self, time=None, xloc=None, yloc=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MULTICOMB(Effect):
    """MULTICOMB(outsk, insk, dur, AMP, combfreqlo (Hz), combfreqhi (Hz), REVERBTIME[, inputchan, ringdowndur])"""
    instrument = "MULTICOMB"
    pfields = 'amp', 'reverbtime'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, combfreqlo=None, combfreqhi=None, reverbtime=None, inputchan=None, ringdowndur=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class MULTEQ(Effect):
    """MULTEQ(outsk, insk, dur, AMP, MASTERBYPASS, EQTYPE1, FILTFREQ1, FILTQ1, FILTAMP1, FILTBYPASS1, ... EQTYPEN, FILTFREQN, FILTQN, FILTAMPN, FILTBYPASSN)"""
    instrument = "MULTEQ"
    pfields = 'amp', 'masterbypass'
    kw_pattern = 'eqtype', 'filtfreq', 'filtq', 'filtamp', 'filtbypass'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, masterbypass=None, eqtype1=None, filtfreq1=None, filtq1=None, filtamp1=None, filtbypass1=None, *extra_args, **extra_kwargs):
        self._passback(locals()) 
class NPAN(Effect):
    """NPAN(outsk, insk, dur, AMP, mode, ANGLE/XLOC, DISTANCE/YLOC[, inputchan])"""
    instrument = "NPAN"
    pfields = 'amp', 'angle', 'distance'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, mode=None, angle=None, distance=None, inputchan=None, *extra_args, **extra_kwargs):
        self._passback(locals()) 
class PAN(Effect):
    """PAN(outsk, insk, dur, amp[, inputchan, panmode, panenv])"""
    instrument = "PAN"
    pfields = 'amp', 'panmode', 'panenv'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, inputchan=None, panmode=None, panenv=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class PANECHO(Effect):
    """PANECHO(outsk, insk, dur, AMP, CHAN_0_DELAY, CHAN_1_DELAY, FEEDBACK, ringdowndur[, inputchan])"""
    instrument = "PANECHO"
    pfields = 'amp', 'chan_0_delay', 'chan_1_delay', 'feedback'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, chan_0_delay=None, chan_1_delay=None, feedback=None, ringdowndur=None, inputchan=None, *extra_args, **extra_kwargs):
        self._passback(locals()) 
class PLACE(Effect):
    """PLACE(outskip, inskip, dur, AMP, dist-xpos, angle-ypos, (-)dist_between_mikes, reverb_amp[, input_channel)"""
    instrument = "PLACE"
    pfields = 'amp',
    def __init__(self, outskip=None, inskip=None, dur=None, amp=None, dist_xpos=None, angle_ypos=None, dist_between_mikes=None, reverb_amp=None, input_channel=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class PVOC(Effect):
    """PVOC(outsk, insk, dur, amp, inputchan, fftsize, windowsize, decimation, interpolation[, pitchmult, npoles, oscthreshold])"""
    instrument = "PVOC"
    pfields = ()
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, inputchan=None, fftsize=None, windowsize=None, decimation=None, interpolation=None, pitchmult=None, npoles=None, oscthreshold=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class QPAN(Effect):
    """QPAN(outsk, insk, dur, amp, xloc, yloc[, inputchan])"""
    instrument = "QPAN"
    pfields = 'amp', 'xloc', 'yloc'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, xloc=None, yloc=None, inputchan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class REV(Effect):
    """REV(outsk, insk, dur, amp, rvbtype, rvbtime, rvbpercent[, inputchan])"""
    instrument = "REV"
    pfields = 'amp', 'rvbamt'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, rvbtype=None, rvbtime=None, rvbamt=None, inputchan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class REVERBIT(Effect):
    """REVERBIT(outsk, insk, dur, amp, rvbtime, rvbpercent, chan0delay, filtfreq (Hz)[, dcblock, ringdowndur])"""
    instrument = "REVERBIT"
    pfields = 'amp', 'rvbtime', 'rvbamt', 'filtfreq'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, rvbtime=None, rvbamt=None, chan0delay=None, filtfreq=None, dcblock=None, ringdowndur=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class REVMIX(Effect):
    """REVMIX(outsk, insk, dur, AMP[, inputchan, PAN])"""
    instrument = "REVMIX"
    pfields = 'amp', 'pan'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class ROOM(Effect):
    """ROOM(outsk, insk, dur, amp[, inputchan])"""
    instrument = "ROOM"
    pfields = ()
    def __init__(self, xsize=None, ysize=None, xsrc=None, ysrc=None, xleftwall=None, yleftwall=None, xrightwall=None, yrightwall=None, absorpt=None, seed=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class SCRUB(Effect):
    """SCRUB(outsk, insk, outdur, AMP, SPEEDMULT, syncwidth, oversampling[, inputchan, pan])"""
    instrument = "SCRUB"
    pfields = 'amp', 'speedmult'
    def __init__(self, outsk=None, insk=None, outdur=None, amp=None, speedmult=None, syncwidth=None, oversampling=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class SHAPE(Effect):
    """SHAPE(outsk, insk, dur, amp, mindist, maxdist, ampnormtable[, inputchan, pan {default: 0.5}, transferfunc, indexguide])"""
    instrument = "SHAPE"
    pfields = 'amp', 'mindist', 'maxdist', 'ampnormtable', 'pan', 'transferfunc', 'indexenv'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, mindist=None, maxdist=None, ampnormtable=None, inputchan=None, pan=None, transferfunc=None, indexenv=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class SPECTACLE(Effect):
    """SPECTACLE(outsk, insk, dur, amp, ringdowndur, fftsize, windowsize, windowtype, overlap[, sigmix {default: 1}, inputchan, pan {default: 0.5}])"""
    instrument = "SPECTACLE"
    pfields = ()
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, ringdowndur=None, fftsize=None, windowsize=None, windowtype=None, overlap=None, sigmix=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class SPECTACLE2(Effect):
    """SPECTACLE2(outsk, insk, dur, outamp, inamp, ringdowndur, fftsize, windowsize, windowtable, overlap, EQtable, delaytable, feedbacktable[, minEQfreq (Hz), maxEQfreq (Hz) {default: Nyquist}, mindelayfreq (Hz), maxdelayfreq (Hz) {default: Nyquist}, sigmix {default: 1}, inputchan, pan {default: 0.5}])"""
    instrument = "SPECTACLE2"
    pfields = 'outamp', 'inamp', 'windowtable', 'eqtable', 'delaytable', 'feedbacktable', 'mineqfreq', 'maxeqfreq', 'mindelayfreq', 'maxdelayfreq', 'binmaptable', 'wetdrymix', 'pan'
    def __init__(self, outsk=None, insk=None, indur=None, outamp=None, inamp=None, ringdowndur=None, fftsize=None, windowsize=None, windowtable=None, overlap=None, eqtable=None, delaytable=None, feedbacktable=None, mineqfreq=None, maxeqfreq=None, mindelayfreq=None, maxdelayfreq=None, binmaptable=None, wetdrymix=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class SPECTEQ(Effect):
    """SPECTEQ(outsk, insk, dur, amp, ringdowndur, fftsize, windowsize, windowtype, overlap[, inputchan, pan {default: 0.5}])"""
    instrument = "SPECTEQ"
    pfields = ()
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, ringdowndur=None, fftsize=None, windowsize=None, windowtype=None, overlap=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class SPECTEQ2(Effect):
    """SPECTEQ2(outsk, insk, dur, amp, fftsize, windowsize, windowtable, overlap, EQtable[, minfreq (Hz), maxfreq (Hz) {default: Nyquist}, bypass, inputchan, pan {default: 0.5}])"""
    instrument = "SPECTEQ2"
    pfields = 'amp', 'windowtable', 'eqtable', 'minfreq', 'maxfreq', 'bypass', 'pan'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, fftsize=None, windowsize=None, windowtable=None, overlap=None, eqtable=None, minfreq=None, maxfreq=None, bypass=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class SPLITTER(Effect):
    """SPLITTER(outsk, insk, dur, GLOBAL_AMP, input_channel, OUTCHAN0_AMP, OUTCHAN1_AMP, ...)"""
    instrument = "SPLITTER"
    pfields = 'global_amp'
    kw_pattern = 'outchan_amp'
    def __init__(self, outsk=None, insk=None, dur=None, global_amp=None, input_channel=None, *extra_args, **extra_kwargs):
        self._passback(locals()) 
class SROOM(Effect):
    """SROOM(outsk, insk, dur, amp, rightdist, frontdist, xloc, yloc, rvbtime, reflect, inroomwidth[, inputchan])"""
    instrument = "SROOM"
    pfields = ()
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, rightdist=None, frontdist=None, xloc=None, yloc=None, rvbtime=None, reflect=None, inroomwidth=None, inputchan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class STEREO(Effect):
    """STEREO(outsk, insk, dur, AMP, P4-N: input/output channel pan assigns)"""
    instrument = "STEREO"
    pfields = 'amp'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class STGRANR(Effect):
    instrument = "STGRANR"
    pfields = ()
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, rate=None, *extra_args, **extra_kwargs):
        self._passback(locals()) 
class TRANS(Effect):
    """TRANS(outsk, insk, dur, AMP, TRANSP[, inputchan, PAN])"""
    instrument = "TRANS"
    pfields = 'amp', 'transp', 'pan'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, transp=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class TRANS3(Effect):
    """TRANS3(outsk, insk, dur, AMP, TRANSP[, inputchan, PAN])"""
    instrument = "TRANS3"
    pfields = 'amp', 'transp', 'pan'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, transp=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class TRANSBEND(Effect):
    """TRANSBEND(outsk, insk, dur, amp, pitchenvgenno[, inputchan, pan])"""
    instrument = "TRANSBEND"
    pfields = ()
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, pitchenvgenno=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class TVSPECTACLE(Effect):
    """TVSPECTACLE(outsk, insk, dur, amp, ringdowndur, fftsize, windowsize, windowtype, overlap[, sigmix {default: 1}, inputchan, pan {default: 0.5}])"""
    instrument = "TVSPECTACLE"
    pfields = ()
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, ringdowndur=None, fftsize=None, windowsize=None, windowtype=None, overlap=None, sigmix=None, inputchan=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals())
class VOCODE2(Effect):
    """VOCODE2(outsk, insk, dur, AMP, nfilts, CFREQLO_FTABLETRANSP, CFREQMULT_FILTMULT, transp, filtbw[, filtresponse, hisigmix, hifreq, NOISEAMP, noiserate, PAN, CFREQTABLE])"""
    instrument = "VOCODE2"
    pfields = 'cfreqlo_ftabletransp', 'cfreqmult_filtmult', 'noiseamp', 'pan', 'cfreqtable'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, nfilts=None, cfreqlo_ftabletransp=None, cfreqmult_filtmult=None, transp=None, filtbw=None, filtresponse=None, hisigmix=None, hifreq=None, noiseamp=None, noiserate=None, pan=None, cfreqtable=None, *extra_args, **extra_kwargs):
        self._passback(locals()) 
class VOCODE3(Effect):
    """VOCODE3(outsk, insk, dur, AMP, MODCFREQS, CARCFREQS, BANDMAP, CAMPSCALE, MODCFTRANSP, CARCFTRANSP, MODFILTQ, CARFILTQ[, FILTRESPONSE, HOLD, PAN])"""
    instrument = "VOCODE3"
    pfields = 'amp', 'modcfreqs', 'carcfreqs', 'bandmap', 'campscale', 'modcftransp', 'carcftrasp', 'modfiltq', 'carfiltq', 'filtresponse', 'hold', 'pan'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, modcfreqs=None, carcfreqs=None, bandmap=None, campscale=None, modcftransp=None, carcftransp=None, modfiltq=None, carfiltq=None, filtresponse=None, hold=None, pan=None, *extra_args, **extra_kwargs):
        self._passback(locals()) 
class VOCODESYNTH(Effect):
    """VOCODESYNTH(outsk, insk, dur, AMP, nfilts, CFREQLO/FTABLETRANSP, CFREQMULT/FTABLEFORMAT, transp, filtbw, windowsize, smoothness, threshold, attack}, release, hisigmix, hifreq, inputchan, PAN, WAVETABLE[, SCALINGTABLE, CFREQTABLE])"""
    instrument = "VOCODESYNTH"
    pfields = 'amp', 'cfreqlo_ftabletransp', 'cfreqmult_ftableformat', 'pan', 'wavetable', 'scalingtable', 'cfreqtable'
    def __init__(self, outsk=None, insk=None, dur=None, amp=None, nfilts=None, cfreqlo_ftabletransp=None, cfreqmult_ftableformat=None, transp=None, filtbw=None, windowsize=None, smoothness=None, threshold=None, attack=None, release=None, hisigmix=None, hifreq=None, inputchan=None, pan=None, wavetable=None, scalingtable=None, cfreqtable=None, *extra_args, **extra_kwargs):
        self._passback(locals()) 
