a = int(input())
if a <= 10:
    print(a * 6)
elif a > 10 and a <= 20:
    print(10*6 + (a-10)*2)
elif a > 20 and a <= 40:
    print(10*6 + 10*2 + (a-20)*1)
else:
    print(100)