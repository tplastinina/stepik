s1, s2 = str(input()), input()
k = 0
s1 = list(s1)
s2 = list(s2)
for j in s2:
    if j in s1:
        k += 1
if k == len(s2):
    print("Да, первая строка содержит все символы второй строки")
else:
    print("Нет, первая строка не содержит все символы второй строки")
