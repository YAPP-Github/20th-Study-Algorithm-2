#17836
from collections import deque
#0: 빈공간, 1: 마법의 벽, 2: 그람
#그람을 구한다면 벽을 뚫을 수 있음
n,m,t = map(int,input().split())
arr =[list(map(int,input().split())) for _ in range(n)]
visited = list([0]*m for _ in range(n)) #방문 여부를

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def save_princess(y,x):
    gram_time  = float("inf")
    queue = deque()
    queue.append((y,x))
    visited[y][x] = 1
    while queue:
        y,x = queue.popleft()
        if (y == n-1 and x == m-1): #끝까지 도달
            return min(visited[-1][-1] - 1, gram_time)

        for i in range(4):
            ny, nx= y+ dy[i], x+ dx[i]
            if (nx < 0 or nx >= m or ny < 0 or ny >= n or visited[ny][nx] or arr[ny][nx] == 1): #벽이 존재할때
                continue
            visited[ny][nx] = visited[y][x] + 1
            queue.append((ny, nx))
            if arr[ny][nx] == 2:
                gram_time = visited[ny][nx]-1 + (n - ny-1) + (m - nx-1)


    return gram_time #끝까지 도달하지 못한 경우


result_time = save_princess(0,0)
print("Fail" if (result_time > t) else result_time)