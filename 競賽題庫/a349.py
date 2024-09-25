ram = [0]*8
cache = [0]*4
for i in range(8):
    ram[i] = int(input())

for i in range(int(input())):
    command  = list(map(str, input().split(" ")))
    if command[0] == "LOAD":
        cache[int(command[1])] = ram[int(command[2])]
    if command[0] == "STORE":
        ram[int(command[1])] = cache[int(command[2])]
    if command[0] == "ADD":
        cache[int(command[1])] = cache[int(command[2])] + cache[int(command[3])]
    if command[0] == "MOVE":
        cache[int(command[1])] = cache[int(command[2])]

print(cache[0])
print(ram[0])

#這題蠻簡單的其實