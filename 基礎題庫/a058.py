a = int(input())
b = []
c = d = e = 0
for i in range(a):
    b.append(int(input()))
for number in b:
    f = number%3
    if f == 0:
        c+=1
    elif f == 1:
        d+=1
    else:
        e+=1
print(c,d,e)

