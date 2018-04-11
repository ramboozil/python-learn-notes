import functools
import time


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        s_time = time.time()
        result = fn(*args, **kwargs)
        e_time = time.time()
        print('%s executed in %s ms' % (fn.__name__, e_time - s_time))
        return result
    return wrapper

