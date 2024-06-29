a,b = map(int, input().split(" "))
s = (a*2+b)%3
if s == 0:
    print("普通")
if s == 1:
    print("吉")
if s == 2:
    print("大吉")