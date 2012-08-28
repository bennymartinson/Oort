class OortError(Exception):
    pass

class OortInstrumentError(OortError):
    pass

class OortBehaviorError(OortError):
    pass

class OortScheduleError(OortError):
    pass

class OortBusError(OortError):
    pass