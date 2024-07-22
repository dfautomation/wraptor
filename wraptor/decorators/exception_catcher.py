from functools import wraps
from six.moves import queue
import sys


def exception_catcher(fn):
    """ Catch exceptions raised by the decorated function.
        Call check() to raise any caught exceptions.
    """
    exceptions = queue.Queue()

    @wraps(fn)
    def wrapped(*args, **kwargs):
        try:
            ret = fn(*args, **kwargs)
        except Exception:
            exceptions.put(sys.exc_info())
            raise
        return ret

    def check():
        try:
            item = exceptions.get(block=False)
            klass, value, tb = item
            raise klass(value).with_traceback(tb)
        except queue.Empty:
            pass

    setattr(wrapped, 'check', check)
    return wrapped
