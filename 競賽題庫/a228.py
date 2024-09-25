num = int(input())
for i in range(num):
    a, b = map(int,input().split(" "))
    room = [0]*a
    for i in range(a):
        room[i] = list(map(int,input().split(" ")))
    
    #待完成