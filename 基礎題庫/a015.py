import sys 
for inp in sys.stdin:
    row,cloumn = list(map(int, inp.split()))
    matrix_list = []
    for i in range(row):
        matrix_list.append(list(map(int, sys.stdin.readline().split())))
    matrix_list = list(zip(*matrix_list)) #現在才知道python有zip可以反轉矩陣
    for ele in matrix_list: print(*ele)
#沒看到多筆測試資料一直沒過
#後來參考了一下這篇 https://hackmd.io/@vientoligero/By_1qbKQp#zerojudge-a015-%E7%9F%A9%E9%99%A3%E7%9A%84%E7%BF%BB%E8%BD%89