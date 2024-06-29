string = input()
code = ""
for i in range (len(string)-1):
    code += str(abs(ord(string[i]) - ord(string[i+1]))) #算出兩個字母的ascii值差異然後取絕對值
print(code)