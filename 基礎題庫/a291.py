from sys import stdin
for s in stdin:
    if s.strip() == '': continue
    correct = list(map(int,s.split(" ")))
    a = int(stdin.readline())
    d = ""
    for i in range(a):
        b = list(map(int,stdin.readline().split(" ")))
        p = q = 0
        c = []
        for i in range(len(b)):
            if b[i] == correct[i]:
                if b[i] in c:
                    q-=1
                p+=1
                c.append(b[i])
            elif (b[i] in correct) and (b[i] not in c):
                q+=1
                c.append(b[i])        
        d += f"{p}A{q}B\n"
print(d)




#TLE有夠嚴格 用上面的寫法把input改成stdin還是沒過
#後來是用下面那篇
#https://steam.oxxostudio.tw/category/python/zerojudge/a291.html
#也是壓秒差點TLE(3s就TLE)
