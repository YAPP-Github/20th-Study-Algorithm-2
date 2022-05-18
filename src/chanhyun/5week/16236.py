from collections import deque

n = int(input())
ocean = []
for _ in range(n):
    ocean.append(list(map(int, input().split())))

def can_eat(i, j):
    q = deque([(i,j)])
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    distance[i][j] = 0
    candidate = []
    while q:
        x, y = q.popleft()
        for d in [(-1,0),(0,1),(1,0),(0,-1)]:
            nx = x + d[0]
            ny = y + d[1]
            if 0<=nx<n and 0<=ny<n and distance[nx][ny] == -1 and ocean[nx][ny] <= baby_s:
                q.append((nx,ny))
                distance[nx][ny] = distance[x][y] + 1
                if 0 < ocean[nx][ny] < baby_s:
                    candidate.append((distance[nx][ny], nx, ny))
    return candidate

baby_s = 2
baby_x = 0
baby_y = 0
for i in range(n):
    for j in range(n):
        if ocean[i][j] == 9:
            baby_x=i
            baby_y=j
            break

time = 0
count = 0
while True:
    candidate = can_eat(baby_x,baby_y)
    if candidate == []:
        break
    else:
        candidate.sort()
        t, x, y = candidate[0]
        time += t
        count += 1
        ocean[baby_x][baby_y] = 0

        baby_x = x
        baby_y = y

        if baby_s == count:
            baby_s += 1
            count = 0

        ocean[x][y] = 9

print(time)