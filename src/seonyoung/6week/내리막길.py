
m,n = map(int,input().split())
mapList =  [list(map(int,input().split())) for _ in range(m)]

visited = [[-1] * n for _ in range (m)]

def dfs(x,y):
    if x==m-1 and y ==n-1:
        return 1
    if visited[x][y]!=-1:
        return int(visited[x][y])
    visited[x][y]=0
    for i in range(4):
        tempX = x + dx[i]
        tempY = y + dy[i]
        if 0 <= tempX < m and 0 <= tempY < n:
            if mapList[tempX][tempY] < mapList[x][y]:
                visited[x][y] += dfs(tempX, tempY)
    return visited[x][y]


dx = [0,0,-1,1]
dy = [1,-1,0,0]

print(dfs(0,0))

