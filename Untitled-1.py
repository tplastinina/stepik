import random
#Угадай число
a=random.randint (0,10)
print ('Какое число загадал компьютер от 0 до 10? Сможешь за пять попыток?')
b=int(input())
i=0
while a!=b:
    print ('ха-ха , а вот и нет, попробуй снова \nя дам тебе подсказку:')
    if a<b:
        print ('ну что-то борщанул, бери меньше')
        i=i+1
    else:
        print ('бери больше')
        i=i+1
    if i==5:
        print ('ема ты лох, я с такими не играю')
    b=int(input())
print ('ты что, Ванга?')



