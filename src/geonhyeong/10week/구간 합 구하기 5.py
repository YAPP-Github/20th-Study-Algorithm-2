# 구간 합 구하기 5.py
# Question Link: https://www.acmicpc.net/problem/11660
# Primary idea:     누적 합
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 1180 ms
# Memory Usage: 70.908 MB

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = [[0] * (n + 1)]
for _ in range(n):
    temp = [0] + list(map(int, input().split()))
    
    # 열 더하기
    for i in range(1, n+1):
        temp[i] += temp[i - 1]
    
    board.append(temp)

# 행 더하기
for j in range(1, n+1):
    for i in range(1, n):
        board[i + 1][j] += board[i][j]

# for b in board:
#     print(b, sep= " ")
# [0, 0, 0, 0, 0]
# [0, 1, 3, 6, 10]
# [0, 3, 8, 15, 24]
# [0, 6, 15, 27, 42]
# [0, 10, 24, 42, 64]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(board[x2][y2] - board[x1 - 1][y2] - board[x2][y1 - 1] + board[x1 - 1][y1 - 1])

# 1번 풀이 - [완탐] 시간 초과
# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     sum = 0

#     for i in range(x1 - 1, x2):
#         for j in range(y1 - 1, y2):
#             sum += board[i][j]
    
#     print(sum)