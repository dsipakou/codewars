class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = []
        self._d = dict()

    def get(self, key: int) -> int:
        if key in self._cache[-self._capacity:]:
            item = self._cache.pop(self._cache.index(key))
            self._cache.append(item)
            return self._d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._cache.pop(self._cache.index(key))
        self._cache.append(key)
        self._d[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)