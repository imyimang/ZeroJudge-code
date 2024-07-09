n = int(input())
for i in range(n):
    m,p = map(float, input().split())
    a = ((p-m) / m)*100
    if a > 0: a += 0.00001
    else: a -= 0.00001
    ans = f"{a:.2f}"
    if ans == "-0.00": ans = "0.00"
    if a >= 10 or a <= -7:
        print(f"{ans}% dispose")
    else:
        print(f"{ans}% keep")

#這題誤差值的部分比較難解決，我是參考討論區的方法加上0.00001
#詳細情況可以參考下面這篇
#https://mousecoding.blogspot.com/2023/09/zerojudge-a647.html