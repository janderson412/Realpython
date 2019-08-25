

def speak(volume):
    def yell(message):
        return message.upper()

    def whisper(message):
        return message.lower()

    if volume < 0.5:
        return whisper
    else:
        return yell

def make_adder(n):
    def add(x):
        return x + n
    return add

class Adder():
    def __init__(self, n):
        self._n = n

    def __call__(self, x):
        return self._n + x


if __name__ == "__main__":
    message = 'Hello'
    loud = speak(.8)
    soft = speak(.3)
    print(f'Loud: {loud(message)} Soft:{soft(message)}')

    add_10 = make_adder(10)
    add_17 = make_adder(17)
    print(f'add_10(20):{add_10(20)}  add_17(38):{add_17(38)}')

    add_101 = Adder(101)
    print(f'add_101(234) = {add_101(234)}')
