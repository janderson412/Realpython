from contextlib import contextmanager
import time

class TimerClass():
    def __init__(self):
        self._start_time = None

    def __enter__(self):
        self._start_time = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = time.perf_counter()
        elapsed_seconds = t - self._start_time
        print(f'Timer() class: Elapsed time:{elapsed_seconds} sec')

def test_func(loop_count):
    x = 10023.34
    y = 45.1
    z = 10
    for _ in range(loop_count):
        z = z * y
        z = z / x
    return z

@contextmanager
def timer():
    try:
        t1 = time.perf_counter()
        yield

    finally:
        t2 = time.perf_counter()
        elapsed = t2 - t1
        print(f'(timer() func: Elapsed time:{elapsed} sec')


if __name__ == "__main__":
    with TimerClass() as t:
        test_func(1000000)

    with TimerClass() as t2:
        test_func(10000000)

    with TimerClass() as t3:
        test_func(50000000)

    with timer() as t:
        test_func(50000000)

