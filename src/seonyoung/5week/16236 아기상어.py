#시뮬레이션
#BFS -> 현재 경로가 젤 최적, 한번이라도 만나면 최단 거리

n = int(input())
sharkMap = [list(map(int,input().split())) for _ in range(n)]
count,time,eatCount,size=0,0,0,2
fishIndex=[]
sharkX, sharkY=0,0

from collections import deque
dx = (0,0,1,-1)
dy = (1,-1,0,0)

def bfs(x,y):
    q=deque([(x,y,0)])
    dist, visited=[], [[False]*n for _ in range(n)] 
    visited[x][y]=True
    minDist = float('inf')

    while q:
        sx,sy,sdist = q.popleft()
        for i in range(4) :#상하좌우
            tempX = dx[i] +sx
            tempY = dy[i]+sy
            if 0<=tempX<n and 0<=tempY<n and not visited[tempX][tempY]:
                if sharkMap[tempX][tempY] <= size:
                    visited[tempX][tempY] = True
                    if 0<sharkMap[tempX][tempY]<size:
                        minDist = sdist
                        dist.append((sdist+1,tempX,tempY))
                    if sdist+1 <= minDist:
                        q.append((tempX,tempY,sdist+1))
    if dist:
        dist.sort()
        return dist[0]
    else :
        return False

            


for i in range(n):
    for j in range(n):
        if 0<sharkMap[i][j]<=6:
            count+=1
            fishIndex.append((i,j))
        elif sharkMap[i][j]==9: #엄마 상어일 경우
            sharkX,sharkY=i,j
sharkMap[sharkX][sharkY]=0 

while count :
    result = bfs(sharkX,sharkY)
    if not result:
        break   
    sharkX,sharkY = result[1],result[2]
    time+=result[0]
    eatCount+=1
    count-=1
    if size==eatCount:
        size+=1
        eatCount=0 
    sharkMap[sharkX][sharkY]=0

print(time)