#14500 테트로미노

#테트로미노(정사각형 네개 겹친)가 높인 칸에 쓰여 있는 수들의 합
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr =[list(map(int,input().split())) for _ in range(n)]
visited = list([0] * m for _ in range(n))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = 0

def dfs(cnt, y, x, total_sum):
    global answer

    if cnt == 4:
        answer = max(answer, total_sum)
        return

    for i in range(4):
        ny, nx = dy[i] + y, dx[i] + x
        if 0 <= ny and ny < n and 0 <= nx and nx < m and visited[ny][nx] == 0:
            if (cnt == 2): #중간 부분
                visited[ny][nx] = 1
                dfs(cnt + 1, y, x, total_sum + arr[ny][nx])
                visited[ny][nx] = 0
            visited[ny][nx] = 1
            dfs(cnt+1, ny, nx, total_sum + arr[ny][nx])
            visited[ny][nx] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(1, i, j, arr[i][j])
        visited[i][j] = 0

print(answer)