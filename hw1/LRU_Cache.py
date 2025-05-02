#Реализация LRUCache

class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.cache = {}
        self.order = {}
        self.counter = 0 

    def get(self, key: str) -> str:
        if key in self.cache:
            self.order[key] = self.counter
            self.counter += 1
            return self.cache[key]
        return ""

    def set(self, key: str, value: str) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.order[key] = self.counter
        else:
            if len(self.cache) >= self.capacity:
                lru_key = min(self.order, key=lambda k: self.order[k])
                del self.cache[lru_key]
                del self.order[lru_key]
            self.cache[key] = value
            self.order[key] = self.counter
        self.counter += 1

    def rem(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]
            del self.order[key]