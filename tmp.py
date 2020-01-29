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


t = Temp()
t.say(5)