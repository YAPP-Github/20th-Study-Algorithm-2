from collections import deque
import math 

def solution(grid, k):
    dx= [-1,0,0,1]
    dy= [0,-1,1,0]
    n,m= len(grid),len(grid[0])
    answerList, zList= [],[]
    answerMap= [[0]*m for i in range(n)]
    mapList=[]
    
    for i in range (len(grid)):
        mapList.append(list(grid[i]))

    dq = deque()
    dq.append((0,0)) 
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and answerMap[nx][ny]!=1:
                if mapList[nx][ny]=='F' or mapList[nx][ny]=='.':
                    answerList.append(mapList[nx][ny])
                    zList.append((nx,ny))
                    dq.append((nx,ny))
                    answerMap[nx][ny]=1

    needNum = math.trunc(len(answerList)/k)
    

    answer=0
    if len(answerList)-2>=k:
        answer = needNum
    return answer