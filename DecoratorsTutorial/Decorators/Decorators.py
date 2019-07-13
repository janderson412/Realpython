import functools
import time

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

def do_twice_with_return(func):
    def wrapper_do_twice_with_return(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice_with_return


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before running function
        value = func(*args, **kwargs)
        # Do something afterward
        return value
    return wrapper_decorator

def timer(func):
    '''Print the runtime of the decorated function'''
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        # Do something before running function
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        # Do something afterward
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'Finished {func.__name__!r} in {run_time:.4f} seconds')
        return value
    return wrapper_timer

def debug(func):
    '''Print the function and arguments'''
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        # Do something before running function
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k,v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')
        value = func(*args, **kwargs)
        # Do something afterward
        print(f'{func.__name__!r} returned {value!r}')
        return value
    return wrapper_debug


def slow_down(func):
    '''Sleep one second'''
    @functools.wraps(func)
    def wrapper_slowdown(*args, **kwargs):
        # Do something before running function
        time.sleep(1)
        value = func(*args, **kwargs)
        # Do something afterward
        return value
    return wrapper_slowdown

