string = input()
new_string = ""
for i in range(len(string)-1,-1,-1):
    new_string += string[i]
print(int(new_string))