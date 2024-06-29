a = int(input())
d = []
for i in range(a):
    c=1
    b = input()
    for j in b:
        c *= int(j)
    d.append(c)
for num in d:
    print(num)