n,k = map(int, input().split())
sList = list(map(int, input().split()))

end,temp, count= 0,0,0
answer=0

for start in range(n):    
    while (count <= k and end < n):     
        
        if sList[end] % 2 == 1: 
            count += 1
        else: 
            temp += 1
        end += 1 
        if start == 0 and end == n:
            answer = temp
            break
        
    if count == k+1 :
        answer = max(temp, answer)
        
    if sList[start] %2 == 1:
        count -= 1
    else: 
        temp -= 1
        


print(answer)