class Buffer:
    def __init__(self): # конструктор без аргументов
        self.val = []

    def add(self, *a): # добавить следующую часть последовательности
        self.val += a
        print(len(self.val))
        while (len(self.val) >= 5):
            self.summ = self.val[0]+self.val[1]+self.val[2]+self.val[3]+self.val[4]
            print(self.summ)
            del self.val[0]
            del self.val[0]
            del self.val[0]
            del self.val[0]
            del self.val[0]
    
    def get_current_part(self):
        print(self.val)
        return self.val
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были     
        # добавлены

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6)
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]
