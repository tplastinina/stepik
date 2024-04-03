n = int(input())
total_3 = 0
n_last = n%10
k_n_last=0
total_ch = 0
summ_5 = 0
pr_7 = 1
sum_0_5 = 0
for i in range(1, n+1):
    a=n%10
    if a==3:
        total_3+=1
    if a==n_last:
        k_n_last+=1
    if a%2 == 0:
        total_ch += 1
    if a>5:
        summ_5+=a
    if a>7:
        pr_7*=a
    if a==0 or n%10==5:
        sum_0_5+=1
    n = n//10
print(total_3, k_n_last, total_ch, summ_5, pr_7, sum_0_5, sep = '\n')