num = int(input())      
for z in range(num):   
    x,y,z,w,n,m = map(int, input().split())       
    role = {'0':0, '1':x, '2':y, '3':-z, '4':-w}  
    try:
        days = input().split()     
        gg = 0                    
        for i in days:
            m = m - gg*n #一開始先中毒，後來才吃飯             
            if m <= 0: break         
            if i == '4': gg = gg + 1 #計算中毒次數
            m = m + role[i]    #計算總體重     
            if m <= 0: break   
        if m <= 0:
            print('bye~Rabbit')       
        else:
            print(f'{m}g')           
    except:
        print(f'{m}g')         
#這題敘述有點複雜，看了很久都寫不出來，後來是看下面解答寫的  
#https://steam.oxxostudio.tw/category/python/zerojudge/a271.html