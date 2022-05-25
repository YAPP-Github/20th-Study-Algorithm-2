def dfs(x,y):
    if x == m-1 and y == n-1:
        return
    for d in [[1,0],[-1,0],[0,1],[0,-1]]:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < m and 0 <= ny < n and road[x][y] > road[nx][ny]:
            if visited[nx][ny] == visited[x][y]:
                visited[nx][ny] += 1
            else:
                visited[nx][ny] = visited[x][y]
            dfs(nx,ny)

m, n = map(int, input().split())
road = []
for _ in range(m):
    road.append(list(map(int, input().split())))

visited = [[0 for _ in range(n)] for _ in range(m)]
visited[0][0] = 1
dfs(0,0)
print(visited[-1][-1])