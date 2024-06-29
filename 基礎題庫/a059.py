a = int(input())
list = {}
for i in range(a):
    list[i] = []
    b = int(input())
    c = int(input())
    for j in range(b,c+1):
        if j**0.5 % 1 == 0:
            list[i].append(j)
for i in list:
    k = 0
    for j in list[i]:
        k+=j
    print(f"Case {i+1}: {k}")
        