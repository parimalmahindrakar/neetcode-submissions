from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ordered_dict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.ordered_dict:
            return -1
        self.ordered_dict.move_to_end(key)
        return self.ordered_dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.ordered_dict:
            self.ordered_dict.move_to_end(key)
        self.ordered_dict[key] = value
        if len(self.ordered_dict) > self.capacity:
            self.ordered_dict.popitem(last=False)

        
