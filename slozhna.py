class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1
    
    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.judge = judge
        self.funcs = funcs
        self.iterable = iterable
           
    def __iter__(self):
        for x in self.iterable:
            pos, neg = 0, 0
            for func in self.funcs:
                if func(x):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield x
                

        # for i in range(len(self.iterable)):
        #     pos, neg = 0, 0
        #     for j in range(len(*funcs)):
        #         if funcs[1](iterable(i)) == True:
        #             pos += 1
        #         else:
        #             neg += 1

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5))) 
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))) 
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all))) 
# [0, 30]