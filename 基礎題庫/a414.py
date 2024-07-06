#極限四行解
import sys
for line in sys.stdin:
    if line.strip()  == "0": break
    print([i for i in bin(int(line) + 1)[2:][::-1]].index("1"))


#正常寫法
import sys

for line in sys.stdin:
    line = line.strip() 
    if line == "0":
        break
    a = bin(int(line) + 1)[2:][::-1] #將數字轉二進位再反轉
    a = [i for i in a] #將二進位字串轉換成list
    print(a.index("1")) #計算第一個"1"在list裡面的索引



#這題要用stdin來抓測資，不然會TLE
#就是將整個字串反轉，然後計算字串在第一個1前面有幾個0，就是他要的答案了