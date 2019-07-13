from Decorators.Decorators import *
import math

@do_twice
def say_whee():
    print("Whee!")


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


@debug
def make_greeting(name, age=None):
    if age is None:
        return f'Howdy {name}!'
    else:
        return f'Howdy {name}, you are {age}'

math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

@slow_down
def countdown(from_number):
    if from_number < 1:
        print('Liftoff!!!')
    else:
        print(from_number)
        countdown(from_number - 1)