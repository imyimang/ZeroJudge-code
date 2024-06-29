while True:
    try:
        a,b = map(int,input().split(" "))
        c = a
        d = 0
        while c<=b:
            a+=1
            d+=1
            c+=a
        print(d+1)
    except EOFError:
        break
