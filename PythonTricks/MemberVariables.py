
class Adder:

    def __init__(self, base):
        self.__base = base

    def add(self, value):
        return self.__base + value

    @property
    def Base(self):
        return self.__base

if __name__ == "__main__":
    adder = Adder(12)
    x = adder.add(45)
    print(f'Adder({adder.Base}).add(45) returns {x}.')
    print(f'Adder class:{dir(adder)}')
    adder._Adder__base = 29
    y = adder.add(4)
    print(f'Adder({adder.Base}).add(4) returns {y}.')

