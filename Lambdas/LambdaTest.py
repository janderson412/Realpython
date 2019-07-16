
add_one = lambda x: x + 1

y = add_one(4)
print(y)

a = (lambda n : n * 4)(8)
print(a)

full_name = lambda last, first, middle: f'Full name:{first} {middle} {last}'
name = full_name('Anderson', 'John', 'E')
print(name)