from collections import deque


n,l,r = map(int,input().split())
nationList = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx,dy =[0,0,-1,1],[-1,1,0,0]
count=0 #이동횟수


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    temp = []
    temp.append((x,y))

    while(queue):
        x,y = queue.popleft()
        for i in range(4):
            tempX = x+ dx[i]
            tempY = y+ dy[i]
            if 0<=tempX<n and 0<=tempY<n and visited[tempX][tempY]==0:
                if l<=abs(nationList[tempX][tempY]-nationList[x][y])<=r:
                    visited[tempX][tempY]=1
                    queue.append((tempX,tempY))
                    temp.append((tempX,tempY))
    return temp

while True:
    flag = False 
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                visited[i][j]=1
                temp = bfs (i,j) # 연결된 국가
                if len(temp)>1: #하나라도 열렸으면 인구이동
                        flag=True
                        for x,y in temp:
                            tempNumber = nationList[x][y]//len(temp)
                        for x,y in temp:
                            nationList[x][y] = tempNumber   
    if flag == False: #더이상 인구이동하지 않은 경우
        break
    count+=1
print(count)
        
