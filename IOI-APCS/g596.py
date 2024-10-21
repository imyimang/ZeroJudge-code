a,b,c = map(int, input().split())
array = [["_"] * a for _ in range(b)]
sort_array = []
index = 0

for i in range(c):
    d,e,f = map(int, input().split())
    if f == 0:
        array[d][e] = "@"
        for j in array[d][e::-1]:
            if j == "@":
                index = e - array[d][e::-1].index("@")
            break
        for i in range(index+1,e):
            array[d][i] = "*"            
    print(array)
# 待完成


        