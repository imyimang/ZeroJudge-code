a, b = input().split(" ")
a, b = int(a), int(b)

"""
for i in range(1,smaller+1):
    if a % i == 0 and b % i == 0 and i > ans:
        ans = i
"""
#我原本是用上面的方法暴力解 但是會TLE(超過執行限定時間)

#看了其他人的教學選擇用下面的輾轉相除法
while a != 0 and b != 0:
    if a > b:
        a = a % b
    elif b > a:
        b = b % a
    else:
        break
if a == 0:
    print(b)
else:
    print(a)
    
