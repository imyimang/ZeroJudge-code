#建立一個字典來管理字母對應的數字
id_number_dict = {
    "A":[10,"台北市"],
    "B":[11,"台中市"],
    "C":[12,"基隆市"],
    "D":[13,"台南市"],
    "E":[14,"高雄市"],
    "F":[15,"台北縣"],
    "G":[16,"宜蘭縣"],
    "H":[17,"桃園縣"],
    "I":[34,"嘉義市"],
    "J":[18,"新竹縣"],
    "K":[19,"苗栗縣"],
    "L":[20,"台中縣"],
    "M":[21,"南投縣"],
    "N":[22,"彰化縣"],
    "O":[35,"新竹市"],
    "P":[23,"雲林縣"],
    "Q":[24,"嘉義縣"],
    "R":[25,"台南縣"],
    "S":[26,"高雄縣"],
    "T":[27,"屏東縣"],
    "U":[28,"花蓮縣"],
    "V":[29,"台東縣"],
    "W":[32,"金門縣"],
    "X":[30,"澎湖縣"],
    "Y":[31,"陽明山"],
    "Z":[33,"連江縣"]
}

id_number = input()
alphabet = id_number_dict[id_number[0]][0]
first_number = alphabet%10*9 + alphabet//10
id_number = id_number[1:]
number_sum = 0
x = 0

for i in range(8,0,-1):
    number_sum += int(id_number[x])*i
    x+=1

number_sum += int(id_number[-1]) + first_number

if number_sum%10 == 0:
    print("real")
else:
    print("fake")
    
