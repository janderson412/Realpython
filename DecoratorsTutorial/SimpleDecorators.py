from datetime import datetime

def my_decorator(func):
    def wrapper():
        print("Something is happening before call")
        func()
        print("Something is happening after call")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()

