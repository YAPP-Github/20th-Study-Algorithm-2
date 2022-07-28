# 정수 삼각형.py
# Question Link: https://school.programmers.co.kr/learn/courses/30/lessons/43105
# Primary idea:     String
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB


def solution(triangle):
    dp = []

    for row in range(1, len(triangle)): # 첫번째(0)는 할 필요없음
        for col in range(row+1):
            if col == 0: # 가장 왼쪽
                triangle[row][0] += triangle[row-1][0]
            elif col == row: # 가장 오른쪽
                triangle[row][-1] += triangle[row-1][-1]
            else: # 중간
                triangle[row][col] += max(triangle[row-1][col-1], triangle[row-1][col])

    return max(triangle[-1])
# triangle : [[7], [10, 15], [18, 16, 15], [20, 25, 20, 19], [24, 30, 27, 26, 24]]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))