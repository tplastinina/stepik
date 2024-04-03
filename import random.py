import random
print ('Добро пожаловать в числовую угадайку')

def is_valid(stroka, r):
    if (stroka.isdigit() == True) and ((int(stroka) >= 1) and (int(stroka) <= r)):
        return True
    else:
        print('А может быть все-таки введем целое число от 1 до', r,'?')
        return False

def ygad(n):
    m = input('Угадайте число которое я загадала: ')   
    k = 0
    if is_valid(m, r) == True:
        while m!=n:
            if m<n:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                k+=1

            elif m>n:
                print('Ваше число больше загаданного, попробуйте еще разок')
                k+=1

        if m==n:
            print('Вы угадали, c', k, 'попыток! поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            return True
    



r = input('До какого числа угадваем?')
ygad(random.randint(1,int(r)))



        
    



    