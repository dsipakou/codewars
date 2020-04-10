class Node:
    def __init__(self, val, min_val, prev):
        self.val = val
        self.min_val = min_val
        self.prev = prev
        

class MinStack:

    def __init__(self):
        self.last = None

    def push(self, x: int) -> None:
        self.prev = self.last
        if self.last:
            min_val = min(self.last.min_val, x)
        else:
            min_val = x
        self.last = Node(x, min_val, self.prev)

    def pop(self) -> None:
        self.last = self.last.prev

    def top(self) -> int:
        return self.last.val

    def getMin(self) -> int:
        return self.last.min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()