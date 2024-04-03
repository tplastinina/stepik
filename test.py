class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x < 0:
            raise NonPositiveError      
        else:
            super().append(x)



class BadName(Exception):
    pass

def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name + " is inappropriate name")
    

while True:
    try:
        name = input("Please enter your name ")
        greeting = greet(name)
        print(greeting)
    except BadName:
        print("Please try again!")
    else:
        break

