# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        parent = (len(array) - 2) // 2
        for parent in range(parent, -1, -1):
            self.siftDown(parent, array)
        return array

    def siftDown(self, index, array):
        _index = index
        while _index < len(array):
            child = _index * 2 + 1
            if child < len(array):
                min_child = child
            else:
                break
            child = _index * 2 + 2
            if child < len(array) and array[child] < array[min_child]:
                min_child = child
            if array[_index] > array[min_child]:
                array[_index], array[min_child] = array[min_child], array[_index]
                _index = min_child
            else:
                break

    def siftUp(self, array):
        index = len(array) - 1
        while index > 0:
            parent = (index - 1) // 2
            if array[index] < array[parent]:
                array[index], array[parent] = array[parent], array[index]
                index = parent
            else:
                break
        return array

    def peek(self):
        # Write your code here.
        pass

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop(-1)
        self.siftDown(0, self.heap)

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.heap)




heap = MinHeap([10,9,8,7,6,5,4,3,2,1])
print(heap.heap)