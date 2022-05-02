from collections import deque

n, m, t = map(int, input().split())
castle = []
for _ in range(n):
    castle.append(list(map(int, input().split())))

distance = [[1e9 for _ in range(m)] for _ in range(n)]
q = deque([])
q.append([0,0])
distance[0][0] = 0
sword = []
while q:
    x, y = q.popleft()
    for d in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx = x + d[0]
        ny = y + d[1]
        if 0<=nx<n and 0<=ny<m and castle[nx][ny] != 1 and distance[nx][ny] > distance[x][y] + 1:
            q.append([nx,ny])
            distance[nx][ny] = distance[x][y] + 1
            if castle[nx][ny] == 2:
                sword = [nx,ny]

answer = distance[-1][-1]
if sword != [] :
    sword_distance = distance[sword[0]][sword[1]] + (n-1 - sword[0]) + (m-1 - sword[1])
    answer = min(distance[-1][-1], sword_distance)
if answer <= t:
    print(answer)
else:
    print("Fail")