from abc import ABC, abstractmethod
import sys

class Base(ABC):
    def __init__(self, value):
        self._value = value

    @property
    def Value(self):
        return self._value

    @abstractmethod
    def Update(self, *args, **kwargs):
        pass

class ModifierIncomplete(Base):
    def __init__(self, value):
        super().__init__(value)

    # does not implement Update() method

class Modifier(Base):
    def __init__(self, value):
        super().__init__(value)

    def Update(self, *args, **kwargs):
        if 'incr' in kwargs:
            self._value += kwargs['incr']
        if 'decr' in kwargs:
            self._value -= kwargs['decr']
        if 'div' in kwargs:
            self._value /= kwargs['div']
        if 'mult' in kwargs:
            self._value *= kwargs['mult']

if __name__ == '__main__':

    try:
        print('Instantiate Base...')
        base = Base(100)
        print(f'Base instantiated OK, value={base.Value}')
    except Exception:
        type, value, traceback = sys.exc_info()
        print(f'Exception instantiating Base: {type.__name__}: {value}')

    try:
        print('Instantiate ModifierIncomplete')
        modifierIncomplete = ModifierIncomplete(200)
        print(f'ModifierIncomplete instantiated OK, value={modifierIncomplete.Value}')
    except Exception:
        type, value, traceback = sys.exc_info()
        print(f'Exception instantiating ModifierIncomplete: {type.__name__}: {value}')

    try:
        print('Instantiate Modifier')
        modifier = Modifier(169)
        print(f'Modifier instantiated OK, value={modifier.Value}')
        modifier.Update(incr=50)
        print(f'Increment by 50, value={modifier.Value}')
        modifier.Update(decr=19)
        print(f'Decrement by 19, value={modifier.Value}')
        modifier.Update(div=53, mult=8)
        print(f'Divide by 53, multiply by 8, value={modifier.Value}')
    except Exception:
        type, value, traceback = sys.exc_info()
        print(f'Exception: {type.__name__}: {value}')
