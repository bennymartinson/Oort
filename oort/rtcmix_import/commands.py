try:
    from rtcmix import addgens, ampdb, autocorrect, boost, bt, bus_config, CHANS, chans, constrain, control_rate, convolve, copygen, copytable, cos, cparam, cpath, cpslet, cpsmidi, cpsoct, cpspch, create_scale, dataset, dbamp, denoise, diapason, dumptable, DUR, dur, ellset, eqtemp, error, fdump, filechans, filedc, filedur, filepeak, filerms, filesr, fplot, freset, gaussrand, get_spray, getamp, getdry, getpch, getrange, getring, getwarp, grand, gravy, highrand, infile, info, init_filter, input, invertgen, irand, just, LEFT_PEAK, left_peak, ln, load, lowrand, lpcstuff, makeLFO, makeconnection, makeconverter, makefilter, makegen, makemonitor, makerandom, maketable, map, matrix, meantone, midipch, mikes, mikes_off, mod, modtable, mrotate, multgens, myscale, note_exists, NPANspeakers, numtest, octcps, octlet, octpch, offsetgen, oldmatrix, output, param, partch, path, path_p, pchadd, pchcps, pchlet, pchmidi, pchoct, PEAK, peak, peakoff, pickrand, pickwrand, plottable, print_off, print_on, prob, punch, pythag, quantizegen, rand, random, rates, reset, resetamp, reversegen, RIGHT_PEAK, right_peak, roomset, rotate, rtinput, rtoutput, rtsetparams, sampfunc, sampfunci, samptable, scalegen, set_attenuation_params, set_filter, set_hnfactor, set_option, set_thresh, setdev, setdevfactor, setdry, setexp, setline, setline_size, setrange, setring, setup, setwarp, setwindow, sfclean, sfcopy, sfprint, sgran, shiftgen, sin, space, speakerloc, speakerloc_p, spray_init, SR, sr, srand, stgran, tablelen, tablemax, tablemin, tb, tbase, tempo, threshold, timeset, trand, translen, trirand, trunc, vMIX, wow, wrap, young
    dummy = False
except ImportError:
    dummy = True

    def dummyCommand(*args, **kwargs):
        pass
    
    def returnNum(*args, **kwargs):
        return 0
    
    addgens = ampdb = autocorrect = boost = bt = bus_config = CHANS = chans = constrain = control_rate = convolve = copygen = copytable = cos = cparam = cpath = cpslet = cpsmidi = cpsoct = cpspch = create_scale = dataset = dbamp = denoise = diapason = dumptable = DUR = dur = ellset = eqtemp = error = fdump = filechans = filedc = filedur = filepeak = filerms = filesr = fplot = freset = gaussrand = get_spray = getamp = getdry = getpch = getrange = getring = getwarp = grand = gravy = highrand = infile = info = init_filter = input = invertgen = irand = just = LEFT_PEAK = left_peak = ln = load = lowrand = lpcstuff = makeLFO = makeconnection = makeconverter = makefilter = makegen = makemonitor = makerandom = maketable = map = matrix = meantone = midipch = mikes = mikes_off = mod = modtable = mrotate = multgens = myscale = note_exists = NPANspeakers = numtest = octcps = octlet = octpch = offsetgen = oldmatrix = output = param = partch = path = path_p = pchadd = pchcps = pchlet = pchmidi = pchoct = PEAK = peak = peakoff = pickrand = pickwrand = plottable = print_off = print_on = prob = punch = pythag = quantizegen = rand = random = rates = reset = resetamp = reversegen = RIGHT_PEAK = right_peak = roomset = rotate = rtinput = rtoutput = rtsetparams = sampfunc = sampfunci = samptable = scalegen = set_attenuation_params = set_filter = set_hnfactor = set_option = set_thresh = setdev = setdevfactor = setdry = setexp = setline = setline_size = setrange = setring = setup = setwarp = setwindow = sfclean = sfcopy = sfprint = sgran = shiftgen = sin = space = speakerloc = speakerloc_p = spray_init = SR = sr = srand = stgran = tablelen = tablemax = tablemin = tb = tbase = tempo = threshold = timeset = trand = translen = trirand = trunc = vMIX = wow = wrap = young = dummyCommand
    
    tablelen = maketable = samptable = returnNum

def _oort_mod_functions():
    """We encapsulate all wrappers here so they don't show up in the oort package"""
    
    global rtsetparams, load, print_on, print_off, control_rate, reset, bus_config
    
    def track_rtsetparams(fn):
        def tr(sampling_rate=44100, num_channels=2, buffer_size=4096):
            _params['sampling_rate'] = sampling_rate
            _params['num_channels'] = num_channels
            _params['buffer_size'] = buffer_size
            fn(sampling_rate, num_channels, buffer_size)
        return tr
    rtsetparams = track_rtsetparams(rtsetparams)
    
    def track_print_off(fn):
        def rpo():
            _params['is_print_on'] = False
            fn()
        return rpo
    print_off = track_print_off(print_off)
    
    def track_print_on(fn):
        def rpo():
            _params['is_print_on'] = True
            fn()
        return rpo
    print_on = track_print_on(print_on)
    
    def track_control_rate(fn):
        def rcr(rate):
            _params['current_control_rate'] = rate
            fn(rate)
        return rcr
    control_rate = track_control_rate(control_rate)
    reset = track_control_rate(reset)    
    
    def track_bus_config(fn):
        def tbc(instrument, *args):
            global current_bus_config
            current_bus_config[instrument] = args
            return fn(instrument, *args)
        return tbc
    bus_config = track_bus_config(bus_config)
    
    def do_once_for_params(fn):
        """Decorator, running fn with specific args only once."""
        done = []
        def run(*args):
            if (args,) not in done:
                done.append((args,))
                fn(*args)
        return run
    load = do_once_for_params(load)
    
    def do_once_ever(fn):
        """Decorator, running fn no more than once ever."""
        done = [] # using mutible object to let closure modify done
        def run(*args):
            if True not in done:
                done.append(True)
                fn(*args)
        return run
    rtsetparams = do_once_ever(rtsetparams)
    
    # commands that require libraries to be loaded
    def load_lib(fn, lib):
        def run(*args):
            load(lib)
            return fn(*args)
        return run
    global pythag, meantone, just, young, partch, eqtemp, create_scale, myscale, setup
    pythag = load_lib(pythag, 'TUNING')
    meantone = load_lib(meantone, 'TUNING')
    just = load_lib(just, 'TUNING')
    young = load_lib(young, 'TUNING')
    partch = load_lib(partch, 'TUNING')
    eqtemp = load_lib(eqtemp, 'TUNING')
    create_scale = load_lib(create_scale, 'TUNING')
    myscale = load_lib(myscale, 'TUNING')
    setup = load_lib(setup, 'IIR')
    
    
_oort_mod_functions()

_params = {
           'is_print_on':True,
           'current_control_rate':1000,
           'sampling_rate':44100,
           'num_channels':2,
           'buffer_size':4096
           }

current_bus_config = {}

def is_print_on():
    return _params['is_print_on']

def current_control_rate():
    return _params['current_control_rate']

def sampling_rate():
    return _params['sampling_rate']

def num_channels():
    return _params['num_channels']

def buffer_size():
    return _params['buffer_size']