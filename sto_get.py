class StockSpanner:

    def __init__(self):
        self._step = 0
        self._indexes = []
        self._values = []
        

    def next(self, price: int) -> int:
        self._step += 1
        print(self._indexes, self._values)
        while len(self._indexes) > 0 and price >= self._values[self._indexes[-1] - 1]:
            self._indexes.pop()
        output = self._step if len(self._indexes) == 0 else self._step - self._indexes[-1]
        self._values.append(price)
        self._indexes.append(self._step)
        return output


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
