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
        print(f'timer() func: Elapsed time:{elapsed} sec')

class Counter():
    def __init__(self, currentValue):
        self.__current_value = currentValue

    @property
    def CurrentValue(self):
        return self.__current_value

    def Decrement(self):
        value = self.__current_value - 1
        if value < 0:
            raise ValueError
        self.__current_value = value
        return value

    def Increment(self):
        self.__current_value += 1
        return self.__current_value

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type != None:
            print(f'Exception caught in context exit: exc_type:[{exc_type}] exc_val:[{exc_val}] exc_tb:[{exc_tb}]')
            return True


if __name__ == "__main__":
    with TimerClass() as t:
        test_func(1000000)

    with TimerClass() as t2:
        test_func(10000000)

    with timer() as t:
        test_func(20000000)

    with Counter(10) as counter:
        for _ in range(12):
            print(f'counter.CurrentValue = {counter.CurrentValue} decrementing...')
            counter.Decrement()
            print(f'counter.CurrentValue = {counter.CurrentValue} after decrement.')

    print(f'Exited with counter.CurrentValue = {counter.CurrentValue}')
