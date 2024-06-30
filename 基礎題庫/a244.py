a = int(input())
for i in range(a):
    b,c,d = map(int,input().split(" "))
    if b == 1:print(c+d)
    if b == 2:print(c-d)
    if b == 3:print(c*d)
    if b == 4:print(c//d)
