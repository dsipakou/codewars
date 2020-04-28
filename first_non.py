class Node:
    def __init__(self, num, prev=None):
        self.prev = None
        self.next = None
        self.value = num
        
class DLL:
    def __init__(self, num):
        self.root = Node(num)
        self.tail = self.root
        
    def add(self, num):
        if not self.root:
            self.__init__(num)
        else:
            node = Node(num)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        
    def remove(self, num):
        node = self.root
        while node:
            if node.value == num:
                if node is self.root:
                    self.root = self.root.next
                else:
                    tmp = node.prev
                    tmp.next = node.next
                break
            node = node.next
                    

class FirstUnique:

    def __init__(self, nums: List[int]):
        self._count = {}
        self.ddl = None
        if len(nums) > 0:
            self.ddl = DLL(nums[0])
            self._count[nums[0]] = False
        for i in range(1, len(nums)):
            self.add(nums[i])
            

    def showFirstUnique(self) -> int:
        node = self.ddl.root
        while node:
            if not self._count.get(node.value, False):
                return node.value
            node = node.next
        else:
            return -1


    def add(self, value: int) -> None:
        if value not in self._count:
            self._count[value] = False
            self.ddl.add(value)
        elif value in self._count:
            self._count[value] = True

        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)