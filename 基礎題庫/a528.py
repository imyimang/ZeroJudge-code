while True:
    try:
        b = []
        a = int(input())
        for i in range(a):
            b.append(int(input()))
        for i in range(a-1):
            for j in range(a-i-1):
                if b[j] > b[j+1]:
                    b[j], b[j+1] = b[j+1], b[j]
        print('\n'.join([str(num) for num in b]))

    except:
        break
#就泡沫排序