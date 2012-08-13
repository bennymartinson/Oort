import threading

class _Schedule:
    registry = None
    time = 0
    
    def __init__(self):
        self.registry = []
        self._append_appendix()
    
    def _get_lock(self, dur):
        """Create a lock and register it"""
        lock = threading.Lock()
        self.registry.append((self.time+dur, lock))
        self.registry.sort()
        lock.acquire()
        return lock
    
    def _release_next(self):
        """Allow the next scheduled event to happen"""
        if len(self.registry):
            time, lock = self.registry.pop(0)
            self.time = time
            lock.release()
    
    def _sprouted_function(self, lock, function, args, **kwargs):
        lock.acquire()
        function(*args, **kwargs)
        self._release_next()
    
    def _appendix(self):
        """This function appends itself to the end of the main thread.
        
        This way we can start a new task when the main thread terminates."""
        #find main thread
        main_thread = None
        threads = threading.enumerate()
        for thread in threads:
            if type(thread) == threading._MainThread:
                main_thread = thread
        main_thread.join()
        self._release_next()
        th = threading.Thread(target=self._wait_for_finish)
        th.start()
    
    def _append_appendix(self):
        th = threading.Thread(target=self._appendix)
        th.start()
        
    def _wait_for_finish(self):
        """ Keep joining with other threads until only self left. """
        current_threads = threading.enumerate()
        while len(current_threads) > 2:
            for thread in current_threads:
                if thread is threading.current_thread() or type(thread) == threading._MainThread:
                    continue
                thread.join()
                break
            current_threads = threading.enumerate()
        self._finish()
    
    def _finish(self):
        """ Do this right before Python terminates. """
        from abstract import total_instrument_plays
        print '_____________________________'
        print 'Oort processing completed.'
        print 'Total instrument plays:', total_instrument_plays
        print 'End time:', current_time()

_schedule = _Schedule()

def current_time():
    return _schedule.time

def wait(dur):
    lock = _schedule._get_lock(dur)
    _schedule._release_next()
    lock.acquire()

def sprout(function, *args, **kwargs):
    lock = _schedule._get_lock(0)
    args = lock,function,args
    th = threading.Thread(target=_schedule._sprouted_function, args=args, kwargs=kwargs)
    th.start()