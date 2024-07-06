import sys

for line in sys.stdin:
    line = line.strip() 
    if line == "0":
        break
    try:
        a = bin(int(line) + 1)[2:][::-1]
        b = 0
        for char in a:
            if char == "1":
                break
            b += 1
        print(b)
    except ValueError:
        continue
#就是將整個字串反轉，然後計算字串到第幾位會從0變成1，就是他要的答案了