class Calk:
    def __init__(self):
        self.val = 0

    def sum(self, a, b):
        print(a+b)
        self.val +=1
        return a+b

    def pro(self, a, b):
        print(a*b)
        self.val +=1
        return a*b
    
    def deli(self, a, b):
        print(a/b)
        self.val +=1
        return a/b
    
    def minu(self, a, b):
        print(a-b)
        self.val +=1
        return a-b
    
Calkulator = Calk()
Calkulator.sum(1345343245, 1336476543343)
Calkulator.pro(12654, 12234)
Calkulator.deli(144, 12)
Calkulator.minu(1234567898765432345678876543, 1)
    