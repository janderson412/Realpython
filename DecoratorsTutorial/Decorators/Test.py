
from Decorators import do_twice
from Decorators import do_twice_with_return

@do_twice
def say_whee():
    print("Whee!")

@do_twice
def greet(name):
    print(f"Hello {name}")


@do_twice_with_return
def return_greeting(name):
    print("Creating greeting")
    return f"Hello {name}"

say_whee()
greet("John")
greet("Pat")

x = return_greeting("Gregory")

print(x)
