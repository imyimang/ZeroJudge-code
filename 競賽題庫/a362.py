a = int(input())
b = []
step = 0
for i in range(a):
    array = list(map(int, input().split(" ")))
    array.append(i)
    b.append(array) #在每個list最後面加一個初始的索引值來方便運算他的最短路徑

b = sorted(b, key=lambda x: (x[0], x[1]))

for i in range(len(b)):
    step += abs(b[i][2] - i)
print(step)

#原本是手搓泡沫排序結果一直TLS，就改成用sorted