class Squares(object):
    def __init__(self, start, stop):
        self.value = start -1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
    
x = Squares(1,10)
ix = iter(x)
next(ix)
next(ix)
list(ix)
for k in Squares(2,9):
    print(k, end = ' ') # prints 4 9 16 25 36 49 64 81 100