while True:
    try:
        a = int(input())
        b = list(map(int, input().split(" ")))
        for i in range(a-1):
            for j in range(a-1):
                if b[j] > b[j+1]:
                    b[j], b[j+1] = b[j+1], b[j]
        print(' '.join([str(num) for num in b]))
    except:
        break
#就是典型的泡沫排序法