from functools import wraps


def log(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log('excute')
def now():
    print('2018-03-27')


now()
