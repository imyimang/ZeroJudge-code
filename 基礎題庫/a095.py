while True:
    try:
        a,b = map(int,input().split(" "))
        if a == b:
            print(b)
        else:
            print(b+1)
    except:
        break

#這題題目寫得有點看無 看下面解答才知道可以這樣無腦解