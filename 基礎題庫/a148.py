while True:
    try:
        number_list = list(map(int, input().split(" ")))
        a = 0
        for i in range(1,number_list[0]+1):
            a+=number_list[i]
        if a/number_list[0]>59:
            print("no")
        else:
            print("yes")
    except EOFError:
        break
