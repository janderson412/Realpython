

def add_one(number):
    '''docstring'''
    return number + 1

def say_hello(name):
    return f"Hello {name}"

def be_aweseome(name):
    return f"Yo {name}, we are awesome!"

def greet_bob(greeter_func):
    return greeter_func('Bob')

n = add_one(6)
print(n)
add_one_also = add_one
z = add_one_also(10)
print(z)

print(say_hello("John"))
print(be_aweseome("Jerry"))

print(say_hello)
print(be_aweseome)

funcs = [say_hello, be_aweseome]
print(funcs[1]("James"))

print(greet_bob(funcs[0]))
print(greet_bob(funcs[1]))
