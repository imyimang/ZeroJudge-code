a,b = map(int, input().split(" "))

number_list = []
for i in range(a,b+1):
    x = 0
    for number in str(i):
        x += int(number) ** len(str(i))
    if x == i:
        number_list.append(i)
if not number_list:
    print("none")
else:
    for num in number_list:
        print(num,end=" ")
