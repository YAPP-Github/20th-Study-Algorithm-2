#신맛은 곱 쓴맛은 합    

from itertools import combinations


n = int(input())
sourList, bitterList =[],[]

for i in range(n):
    sour,bitter=map(int,input().split())
    sourList.append(sour)
    bitterList.append(bitter)


diff=float('inf') #어떤 숫자와 비교해도 무조건 큰쪽으로 판정됨
for i in range(1, n+1):
    tasteList = list(combinations(list(range(n)),i))
    
    for taste in tasteList:
        tempSour,tempBitter=1,0
        for j in range(i):
            tempSour*=sourList[taste[j]]
            tempBitter+=bitterList[taste[j]]
        if abs(tempSour-tempBitter)<diff:
            diff=abs(tempSour-tempBitter)

print (diff)