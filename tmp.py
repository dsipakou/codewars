class Descr:
    def __get__(self, obj, objval):
        return self._value

    def __set__(self, obj, value):
        print('Setter')
        self._value = bin(int(value))[2:]

class Temp:
    x = Descr()

    def say(self, value):
        self.x = value

        print(self.x)


def infinite_gen():
    n = 0
    while True:
        yield n
        n += 1

def check_gen():
    yield("First string")
    yield("Second string")

genn = check_gen()
print([i for i in check_gen()])
print(next(genn))
print(next(genn))