a,b,c = input().split(" ")
if b == "+":
    ans = int(a) + int(c)
if b == "-":
    ans = int(a) - int(c)
if b == "*":
    ans = int(a) * int(c)
if b == "/":
    ans = int(a) // int(c)
print(ans)
#意外的很簡單 如果eval沒被禁會更快