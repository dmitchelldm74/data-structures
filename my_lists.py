class LinkedList:

    def __init__(self):
        """Creates empty LinkedList"""
        self._value = None
        self._next_item = None

    def append(self, val):
        if self._value is None:
            self._value = val
            self._next_item = LinkedList()
        else:
            self._next_item.append(val)

    def __len__(self):
        return 0

    def __getitem__(self, index):
        return None

    def insert(self, index, val):
        pass

    def __repr__(self):
        if self._value is None:
            return "()"
        else:
            return "(%r, %r)" % (self._value, self._next_item)

    # Other methods to consider:
    #   pop, index, remove, reverse
