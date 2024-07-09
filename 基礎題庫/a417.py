a = int(input())
for i in range(a):
    n,m = map(int,input().split())
    if m == 1:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        print(matrix)

#還沒解完