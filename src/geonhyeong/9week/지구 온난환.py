# 지구 온난화.py
# Question Link: https://www.acmicpc.net/problem/5212
# Primary idea:     시뮬레이션
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 88 ms
# Memory Usage: 30.972 MB

import sys
from copy import deepcopy

input = sys.stdin.readline

r, c = map(int, input().split())

# 입력
board = [list(map(str, input().rstrip())) for _ in range(r)]
temp = deepcopy(board) # 깊은 복사

# 동서남북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for x in range(r):
    for y in range(c):
        if temp[x][y] == 'X': # 땅일 경우,
            cnt = 0 # 바다로 둘러 쌓여 있는지 확인

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 범위 밖은 바다를 의미, 원래 바다(.)인지
                if (0 > nx or nx >= r) or (0 > ny or ny >= c) or temp[nx][ny] == '.':
                    cnt += 1

                    if cnt == 3:
                        board[x][y] = '.' # 범람
                        break
                    
island_x = []
island_y = []

# 남은 땅(X) 찾아, 출력할 X, Y 시작, 종료 좌표 찾기
for i in range(r):
    for j in range(c):
        if board[i][j] == 'X':
            island_x.append(i)
            island_y.append(j)

for i in range(min(island_x), max(island_x) + 1):
    for j in range(min(island_y), max(island_y) + 1):
        print(board[i][j], end='')
    print()