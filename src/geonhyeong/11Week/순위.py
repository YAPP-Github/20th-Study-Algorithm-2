# 순위.py
# Question Link: https://school.programmers.co.kr/learn/courses/30/lessons/49191?language=python3
# Primary idea:     그래프
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

def solution(n, results):
    board = [[0] * n for _ in range(n)]

    for p1, p2 in results:
        board[p1 - 1][p2 - 1] = 1     # p1이 p2에 이겼을 때는 1
        board[p2 - 1][p1 - 1] = -1    # p1이 p2에 졌을 때는 -1로 초기화
    
    # 플로이드-와샬
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or board[i][j] in [1, -1]: # 자기 자신과의 경기 or 
                    continue

                if board[i][k] == board[k][j] == 1: # 만약 i가 k에 이겼고, k가 j에 이겼다면
                    board[i][j] = 1
                    board[k][i] = board[j][k] = board[j][i] = -1 # k가 i에 지고, j가 k지면서, j가 i에게도 짐

    res = 0
    for row in board:
        if row.count(0) == 1: # 각 노드 점수판에 0이 하나(다른 노드들에 대해 승패가 모두 결정됨)인 경우
            res += 1
    return res