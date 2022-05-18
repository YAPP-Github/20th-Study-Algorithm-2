# 아기 상어.py
# Question Link: https://www.acmicpc.net/problem/16236
# Primary idea:     구현
#                   1. 함수 구현
#                       1) 물고기를 찾는 함수
#                       2) 각각의 위치까지의 최단거리를 구하는 함수
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 296 ms
# Memory Usage: 32.54 MB

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = []

# 입력
for i in range(N):
    board.append(list(map(int,input().split())))

# 초기화
curX, curY, size = 0, 0, 2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 아기 상어 위치
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            curX, curY = i, j # 위치 저장
            board[curX][curY] = 0 

# 모든 위치까지의 최단거리만 계산
def bfs():
    dist = [[-1] * N for _ in range(N)]
    queue = deque([(curX, curY)])
    dist[curX][curY] = 0  # 아기상어의 위치를 최단거리 0

    while queue:
        x, y = queue.popleft()
        for i in range(4): # 4방향 확인
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] <= size and dist[nx][ny] == -1:
                    queue.append((nx, ny))
                    dist[nx][ny] = dist[x][y]+1
    return dist

# 물고기를 찾는 함수
def find(dist):
    x,y = 0,0
    minDist = float('inf')

    for i in range(N):
        for j in range(N):
            if dist[i][j] != -1 and 1 <= board[i][j] < size: # 물고기까지의 거리와 현재의 최단거리를 비교
                if dist[i][j] < minDist:
                    x,y = i,j
                    minDist = dist[i][j]

    if minDist == float('inf'): # 먹을 물고기가 없는 경우
        return None
    else:
        return x, y, minDist

res = 0
ate = 0

while True:
    value = find(bfs()) # 물고기를 찾고 모든 위치까지의 최단거리만 계산

    if value == None: # 더이상 먹을 물고기가 존재하지 않을 때 까지 반복
        print(res)
        break
    else:
        curX, curY = value[0], value[1] # 아기상어의 현재위치
        res += value[2]                 # 현재 아기상어가 이동한 최단거리, 즉 이동한 시간을 저장
        board[curX][curY] = 0
        ate += 1                        # 자신의 크기와 먹은 물고기의 갯수가 같아질 경우, 
    if ate >= size:                     # ate가 size와 같아지면
        size += 1
        ate = 0