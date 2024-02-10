import time


def timer_func(func):
    """
    Decorator to time function execution

    :param func: function to be timed
    :return: timed function

    """
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'{func.__name__}() executed in {(t2-t1):.6f}s')
        print('')
        return result
    return wrapper



