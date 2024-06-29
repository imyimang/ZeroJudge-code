import math
def is_prime(L,R):
    limit = int(math.sqrt(R)) + 1
    primes = sieve_of_eratosthenes(limit)
    is_prime = [True] * (R - L + 1)

    for prime in primes:
        # 找到範圍 [L, R] 中第一個是 prime 倍數的數字
        start = max(prime*prime, (L + prime - 1) // prime * prime)
        for j in range(start, R + 1, prime):
            is_prime[j - L] = False

    if L == 1:
        is_prime[0] = False

    return [i + L for i in range(R - L + 1) if is_prime[i]]
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

while True:
    try:
        a,b = map(int, input().split(" "))
        c = 0
        print(len(is_prime(a,b)))
    except:
        break


#這題TLE真的太嚴格 我後來用gpt寫了一個Segmented Sieve(類似進階版的埃拉托色尼篩法)的解法，下面是原本的寫法
"""
while True:
    try:
        a,b = map(int, input().split(" "))
        c = 0
        for i in range(a,b+1):
            if i % 6 == 1 or i % 6 == 5:
                d=0
                for j in range(1,i//2):
                    if i%j == 0:
                        d+=1
                if d == 1:
                    c+=1
        print(c)
    except:
        break
"""