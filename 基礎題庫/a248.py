from decimal import Decimal, getcontext
while True:
    try:
        a,b,c = map(int, input().split(" "))
        getcontext().prec = c+1000
        ans = f"{Decimal(a)/Decimal(b):.{c+10}f}"
        print(ans[:-10])
    except EOFError:
        break
#我一開始是直接除然後用f string取小數點，但這樣到後面精度會差很多
#所以後來用decimal函式庫