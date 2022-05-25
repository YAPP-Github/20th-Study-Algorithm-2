# 내리막 길.py
# Question Link: 
# Primary idea:     DP
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

import sys
input = sys.stdin.readline

def outOfIndex(x, y):
    return 0 <= x < M and 0 <= y < N

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if not outOfIndex(nx, ny): continue

            if board[nx][ny] < board[x][y]:
                dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]


M, N = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dp = [[-1 for i in range(N)] for j in range(M)]
board = []

# input
for i in range(M):
    board.append(list(map(int, input().split())))

print(dfs(0, 0))
print(dp)