class MyRangeGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyRangeGen.current < self.last:
            num = MyRangeGen.current
            MyRangeGen.current += 1
            return num
        raise StopIteration


gen = MyRangeGen(0, 10)
for i in gen:
    print(i)
