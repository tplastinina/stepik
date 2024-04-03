import random

class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i -1]
        else:
            raise StopIteration

def random_generation(k):
    for i in range(k):
        yield random()
gen = random_generation(3)
print(type(gen))



class MyList(list):
    def __init__(self, lst):
        self.lst = lst
    def __iter__(self):
        return DoubleElementListIterator(self)
    


