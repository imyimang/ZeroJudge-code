string = input()
string_len = len(string)
char = ""
for i in range(string_len-1,-1,-1):
    char += string[i]
if char == string:
    print("yes")
else:
    print("no") 