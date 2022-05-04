#최단거리 문제이기 때문에 bfs사용
#만약 검 발견하면 직선거리로 계산, 아닐경우 BFS 계산

from collections import deque
dx,dy=[-1,1,0,0],[0,0,-1,1]

def bfs(startNode):
    dist=0
    queue =[]
    queue.append((startNode,dist)) #시작노드
    visited[startNode][dist]=1
    
    while len(queue)>0:
        x,y = queue.pop()       
        if graph[x][y]=='2':  
            dist= (n-x-1)+(m-y-1)+visited[x][y]-1
        if x==n-1 and y==m-1: #공주한테 도착했을 경우
            return min(visited[x][y]-1,dist) #검을 발견한 경우와 그냥 왔을 때 중 더 짧은 거리
        
        for i in range (4):
            nx,ny =x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]!='1':#마법 벽이 아닐 때
                if visited[nx][y]==0: 
                    print('여기로 들어와야함')
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y]+1
        print(visited)
    return dist

n,m,time = map(int,input().split())
graph = [list(input()) for _ in range(n)]
visited =[[0] * m for _ in range(n)]

answer = bfs()
print(answer)
print("Fail" if answer>time else answer)