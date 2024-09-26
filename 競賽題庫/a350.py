while True:
    try:
        long = int(input())
        number = list(map(int, input().split(" ")))
        sum = 0
        flower = [8,16,24,32,40,48,56,64,80]
        last_index = -1
        first_index = 0
        for i in range(len(number)-1, -1, -1):
            if number[i] != 0:
                last_index = i
                break
        for i in range(len(number)):
            if number[i] != 0:
                first_index = i
                break

        if long < flower[last_index]:
            print("NO SOLUTION!!")
            break
        
        # for j in range(len(number)):
        #     if number[j] != 0:
        #         while number[j] != 0:
        #             if long/(number[j]* flower[j]) % 1 == 0:
        #                 sum += long//(number[j]* flower[j])
        #                 number[j] -= long//number[j] + 1
        #             else:
        #                 sum += long//(number[j] * flower[j]) + 1
        #                 number[j] -= long//number[j] + 1


        #         if ((long / flower[-(j+1)] - long / flower[-(j+1)] // 1)* flower[-(j+1)]) < number[first_index]

# 解不開肏
    except EOFError:
        break
