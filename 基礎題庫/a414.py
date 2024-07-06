import sys

for line in sys.stdin:
    line = line.strip() 
    if line == "0":
        break
    try:
        a = [i for i in bin(int(line) + 1)[2:][::-1]]
        print(a.index("1"))
    except ValueError:
        continue
#就是將整個字串反轉，然後計算字串到第幾位會從0變成1，就是他要的答案了