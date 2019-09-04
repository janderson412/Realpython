from statistics import mean
from functools import reduce

def second(x):
    return x[1]

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __repr__(self):
        return f'{self._name}: {self._age}'



if __name__ == '__main__':
    a = [(1,2),(2,5),(3,1),(4,15)]
    print(f'a={a}')
    #a.sort(key=second)
    a.sort(key=lambda x:x[1])
    print(f'a={a} (after sort)')

    power = lambda x, y=2: x **y
    print(f'power(10,0.5)={power(10,0.5)} power(5)={power(5)}')

    #
    # sort()
    #
    names=['John Anderson', 'James Madison', 'Jack Hornblower', 'Howard Baker']
    names.sort(key=lambda x: x.split()[-1].lower())
    print(names)

    john = Person('John', 63)
    linda = Person('Linda', 34)
    betty = Person('Betty', 47)
    p = [john, linda, betty]

    print(p)
    p.sort(key=lambda x: x._age)
    print(p)
    p.sort(key=lambda x: x._name)
    print(p)

    #
    # filter()
    #
    nums = list(range(1, 21))
    print(nums)
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print(evens)

    avg = mean(nums)
    above_avg = list(filter(lambda x: x > avg, nums))
    print(f'> avg({avg}): {above_avg}')

    #
    # map()
    #
    nums = list(range(1, 11))
    print(f'nums={nums}')
    sq_nums = list(map(lambda x: x**2, nums))
    print(f'sq_nums={sq_nums}')

    evens = list(map(lambda x: x % 2 == 0, nums))
    print(f'evens={evens}')

    #
    # reduce()
    #
    nums = list(range(1,11))
    total = reduce(lambda x, y: x + y, nums)
    print(f'total={total}')
    total = reduce(lambda x, y: x + y, nums, 10)
    print(f'total+10={total}')

    names = ['john', 'pat', 'kevin', 'sarah', 'william']
    concat = reduce(lambda x, y: x + y[:2], names)
    print(f'name={names} concat={concat}')
    concat = reduce(lambda x, y: x + y[:2], names, '')
    print(f'name={names} concat={concat}')

