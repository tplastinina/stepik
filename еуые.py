n, k = int(input()), int(input())
def sochetanie_k(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return sochetanie_k(n-1,k) + sochetanie_k(n-1, k-1)
    
print(sochetanie_k(3,2))
print(sochetanie_k(10,5))
