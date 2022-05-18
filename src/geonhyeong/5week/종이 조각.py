# 종이 조각.py
# Question Link: https://www.acmicpc.net/problem/14391
# Primary idea:     완전 탐색
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 480 ms
# Memory Usage: 30.84 MB

N, M = map(int, input().split())

board = []
isVisited = [[False for _ in range(4)] for _ in range(4)]
res = 0

# 입력
for _ in range(N):
    board.append(list(map(int,input())))

def sumTotal():
    total = 0
    for i in range(N):
        rowSum = 0
        for j in range(M):
            if isVisited[i][j]: # 가로 연속
                rowSum = rowSum * 10 + board[i][j]
            else: # 끊길 경우
                total += rowSum
                rowSum = 0
        total += rowSum

    for j in range(M):
        colSum = 0
        for i in range(N):
            if not isVisited[i][j]: # 세로 연속
                colSum = colSum * 10 + board[i][j] 
            else: # 끊길 경우
                total += colSum
                colSum = 0
        total += colSum
    return total

def dfs(x, y):
    global res

    if x == N:
        res = max(res, sumTotal())
        return
    if y == M:
        dfs(x+1, 0)
        return
    
    isVisited[x][y] = True
    dfs(x, y+1) # 가로로 이어졌음
    isVisited[x][y] = False
    dfs(x, y+1) # 세로로 이어졌음

dfs(0, 0)
print(res)