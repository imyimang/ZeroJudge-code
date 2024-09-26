import math

def C(m,n):
    if m<n:
        return 0
    return int(math.factorial(m)/(math.factorial(n) * (math.factorial(m-n))))

times = int(input())
for i in range(times):
    user_input = int(input())
    sum = j = 0
    if user_input == 0:
        print("210")
        continue
    while C(j,3) < user_input:
        j+=1
    k = l = m = j
    while sum != user_input:
        for k in range(j, -1, -1):
            for l in range(j, -1, -1):
                for m in range(j, -1, -1):
                    sum = C(k, 3) + C(l, 2) + C(m, 1)
                    if sum == user_input:
                        print(f"{k}{l}{m}")
                        break
                if sum == user_input:
                    break
            if sum == user_input:
                break
    #先算出a的最大值然後暴力把bc全部求出來
