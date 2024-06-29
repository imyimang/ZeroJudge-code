a = int(input())
while a != 0:
    for i in range(1,a):
        if i%7 != 0:
            print(i,end=" ")
    print()
    a = int(input())