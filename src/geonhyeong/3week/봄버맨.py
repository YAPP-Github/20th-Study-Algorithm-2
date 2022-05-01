# 봄버맨.py
# Question Link: https://www.acmicpc.net/problem/16918
# Primary idea:     BFS, 그래프 이론, 그래프 탐색
#                   1. 3단계와 4단계에 대한 로직을 함수로 구현
#                   2. findBomb()를 통해 터져야하는 bomb의 위치를 구함
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 4440 ms
# Memory Usage: 3477 MB

import sys
from collections import deque
input = sys.stdin.readline

# 출력
def printBoard():
    for i in range(R):
        for j in range(C):
            print(board[i][j], end='')
        print()

# out of boundary
def checkBound(x, y):
    return 0 <= x < R and 0 <= y < C 

# 폭탄의 위치 확인
def findBomb():
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                queue.append([i, j])

# 3단계, 모든 칸에 폭탄 설치
def fillBomb():
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = 'O'

# 4단계, 폭탄이 모두 폭발
def bomb():
    while queue:
        x, y = queue.popleft()
        board[x][y] = '.'
        for i in range(4):
            ddx, ddy = dx[i] + x, dy[i] + y
            if checkBound(ddx, ddy):
                if board[ddx][ddy] == 'O':
                    board[ddx][ddy] = '.'

# 초기 입력
R, C, N = map(int, input().split())

# 선언
board = [[] for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 저장
for i in range(R):
    board[i] = list(input())

N -= 1 # potin! 2단계로 봄버맨이 아무것도 안한 시간
while N > 0:
    queue = deque()
    findBomb() # 폭탄의 위치를 저장
    fillBomb() # 모든 칸에 폭탄 설치
    N -= 1
    if N == 0: break
    bomb() # 폭탄 폭발
    N -= 1

printBoard()    
