
n = int(input())
postArr = str(input())
blueCount, redCount=0,0

if postArr[0]=='B':
    blueCount+=1 
else: 
    redCount+=1

for i in range(1,n):
    if postArr[i]!=postArr[i-1]:
        if postArr[i]=='R':
            redCount+=1
        else:
            blueCount+=1

print(min(redCount,blueCount)+1)    


