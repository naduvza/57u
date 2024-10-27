class CyclicIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.lst:
            raise StopIteration
        value = self.lst[self.index]
        self.index = (self.index + 1) % len(self.lst)
        return value

cyclic_list = CyclicIterator([1, 2, 3])

for i in range(10):
    print(next(cyclic_list))
