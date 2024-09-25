while True:
    try:
        num = int(input())
        num_list = list(map(int,input().split(" ")))
        for i in range(num-1):
            for j in range(num-1):
                if num_list[j] > num_list[j+1]:
                    num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
        if num%2 == 0:
            print((num_list[num // 2] + num_list[num // 2 - 1])/2)
        else:
            print(num_list[(num-1)//2])
    except EOFError:
        break

#欸不是後來我發現他Ram鎖14MB連python都開不了