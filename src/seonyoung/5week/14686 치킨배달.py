

from itertools import combinations


n,m = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(n)]

homeList, chickenList=[],[]
for i in range(n):
    for j in range(n):
        if(map[i][j]==1): #집
            homeList.append((i,j))
        elif(map[i][j]==2):
            chickenList.append((i,j))
    

dist = float('inf')
#치킨 집 중에 하나..
for chicken in combinations(chickenList,m):
    sum=0
    for home in homeList:
        sum+=min([abs(home[0]-tempChicken[0])+abs(home[1]-tempChicken[1]) for tempChicken in chicken])
        if dist<sum:
            break
    if sum<dist:
        dist= sum

print (dist)