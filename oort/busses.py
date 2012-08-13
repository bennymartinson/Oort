import rtcmix_import as rtcmix
from oort.rtcmix_import.commands import current_bus_config
import errors

instrument_backups = {} # dict of previous instrument bus config values
bus_backups = {} # dict of busses and their corresponding instruments that were cleared

def get_bus_config(instrument):
    if instrument in current_bus_config:
        return current_bus_config[instrument]
    else:
        return ('in 0-1', 'out 0-1')

def backup_instrument(instrument):
    """Back up the current bus config for an instrument, so it can be change and restored later."""
    if instrument not in instrument_backups:
        instrument_backups[instrument] = get_bus_config(instrument)

def restore_instrument(instrument):
    if instrument in instrument_backups:
        args = instrument_backups[instrument]
        del instrument_backups[instrument]
        if get_bus_config(instrument) != args:
            rtcmix.bus_config(instrument, *args)
    else:
        raise errors.OortBusError('There are no backed up configs to restore for '+str(instrument))

def clear_instrument(instrument):
    backup_instrument(instrument)
    rtcmix.bus_config(instrument, 'in 0-1', 'out 0-1')

def clear_busses(bus_range):
    instruments = _busses_lookup(bus_range)
    cleared_instruments = []
    for instrument in instruments:
        cleared_instruments.append(instrument)
        clear_instrument(instrument)
    busses = _get_bus_list(bus_range)
    for bus in busses:
        if bus not in bus_backups:
            bus_backups[bus] = set()
        for instrument in instruments:
            bus_backups[bus].add(instrument)
        

def restore_busses(bus_range):
    busses = _get_bus_list(bus_range)
    instruments = set()
    for bus in busses:
        if bus in bus_backups:
            instruments = instruments.union(bus_backups[bus])
            del bus_backups[bus]
    for instrument in instruments:
        restore_instrument(instrument)
        

def _busses_lookup(bus_range):
    """ Finds all instruments that are connected to at least one aux bus in the bus_range, in or out."""
    busses = _get_bus_list(bus_range)
    instruments = []
    for instrument, config in current_bus_config.items():
        inst_busses = set()
        for c in config:
            b = _get_bus_list(c, aux_only=True)
            if b:
                inst_busses = inst_busses.union(b)
        collect = False
        for i in inst_busses:
            if i in busses:
                collect = True 
                break
                # this instrument is connected to at least one bus that's in the bus range
        if collect:
            instruments.append(instrument)
    return instruments

def _get_bus_list(config, aux_only=False):
    """ Returns list of busses from bus_config statement.
    Takes either full statement, or just the bus part (i.e. "0-1").
    If aux_only is True, returns False if 'aux' statement is not present."""
    bus_range = None
    aux = False
    for word in config.split():
        if word == 'aux':
            aux = True
        if word not in ('aux', 'in', 'out'):
            bus_range = word
    if aux_only and not aux:
        return False
    if config.isdigit():
        return [int(config)] # it was just a single number
    try:
        lo, hi = bus_range.split('-')
        if not lo.isdigit() or not hi.isdigit():
            raise
        return range(int(lo), int(hi)+1)
    except:
        raise errors.OortBusError('The config supplied, "'+config+'", is invalid.')