

class Tester:
    staticValue = 100

    def __init__(self, value):
        self._value = value

    def GetValue(self):
        return self._value

    @classmethod
    def GetStaticValue(cls):
        print(f'Class "{cls}" returning staticValue={cls.staticValue}')
        return cls.staticValue

    @staticmethod
    def DoStaticThing(a, b):
        print(f'In DoStaticThing(a={a},b={b})')

class DerivedTester(Tester):
    staticValue = 1000

    def __init__(self, value):
        super().__init__(value)

if __name__ == '__main__':
    t = Tester(900)
    val = t.GetValue()
    sval = Tester.GetStaticValue()
    Tester.DoStaticThing(3, 4)
    print(f'val={val} sval={sval}')

    dt = DerivedTester(555)
    val = dt.GetValue()
    sval = DerivedTester.GetStaticValue()
    DerivedTester.DoStaticThing(88, 99)
    print(f'val={val} sval={sval}')
