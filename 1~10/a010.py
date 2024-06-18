num = int(input())

p = 2
result = []

while p*p <= num: 
    
    times = 0 
    
    while num%p ==0: #求質因數，會一直除直到最後那個數除起來不於1(質數)為止
        times+=1
        num //= p
    
    if times==0: 
        pass
    else: 
        result.append( (p, times) ) 
            
    if num==1:
        break
    p += 1

else: 
    result.append( (num, 1) )

ans = []
for base, power in result:
    if power==1:
        ans.append(str(base)) 
    
    else:
        ans.append(f"{base}^{power}") 
        
print(" * ".join(ans))


#這題我想了很久 最後參考了下面那篇
#https://hackmd.io/@vientoligero/By_1qbKQp#a010