a = int(input())
b = list(map(int, input().split()))
for i in range(a-1):
    for j in range(a-1):
        if b[j] > b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]
print(" ".join(map(str, b)))

if min(b) >= 60:
    print("best case")
else:
    for i in b[::-1]:
        if i < 60:
            print(i)
            break

if max(b) < 60:
    print("worst case")
else:
    for i in b:
        if i >= 60:
            print(i)
            break