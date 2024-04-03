class MoneyBox:
    def __init__(self, capacity): # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.insite = 0 

    def can_add(self, v): # True, если можно добавить v монет, False иначе
        if self.insite + v <= self.capacity:
            return True
        else: 
            return False  

    def add(self, v): # положить v монет в копилку
        if self.can_add(v) == True:
            self.insite += v
            return self.capacity - self.insite
        else:
            return False

x = MoneyBox(15)
x.add(5)
x.add(9)
x.add(3)
