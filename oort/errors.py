class OortError(Exception):
    pass

class OortInstrumentError(OortError):
    pass

class OortBehaviorError(OortError):
    pass

class OortBusError(OortError):
    pass