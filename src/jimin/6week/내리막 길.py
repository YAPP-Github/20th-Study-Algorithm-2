#1520
import sys
input = sys.stdin.readline

m,n = map(int, input().split())
arr =[list(map(int,input().split())) for _ in range(m)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]
dp = [[-1]*n for _ in range(m)]

def dfs(y, x):
    if y == m-1 and x == n-1: #끝까지 도달한 경우
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    for i in range(4):
        ny, nx = dy[i]+y, dx[i]+x
        if (0 <= ny < m and 0 <= nx < n and arr[y][x] > arr[ny][nx]):
            dp[y][x] += dfs(ny, nx)
    print(y,x, dp)
    return dp[y][x]

print(dfs(0,0))

