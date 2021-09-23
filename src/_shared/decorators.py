import time

import simplejson


def step(func):
    """
    debug any class method checking elapsed time and printing data
    """
    pre = func.__qualname__ or func.__name__

    def decorator(*args, **kwargs):
        start_at = time.perf_counter_ns()
        try:
            print(f'{pre}(RUN): ' + simplejson.dumps({'args': args[1:], 'kwargs': kwargs}))
            result = func(*args, **kwargs)
            print(f'{pre}(OK): {simplejson.dumps(result)}')
            return result
        except Exception as e:
            print(f'{pre}(FAIL): {str(e)}')
        finally:
            print(f'${pre}(TIME): {time.perf_counter_ns()-start_at}')

    return decorator
