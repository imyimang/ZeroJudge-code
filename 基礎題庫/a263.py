while True:
    try:
        from datetime import date

        a,b,c = map(int,input().split(" "))
        d,e,f = map(int,input().split(" "))

        date1 = date(a, b, c)
        date2 = date(d, e, f)

        delta = date2 - date1
        print(abs(delta.days))
    except EOFError:
        break
#直接用datetime函式庫偷懶