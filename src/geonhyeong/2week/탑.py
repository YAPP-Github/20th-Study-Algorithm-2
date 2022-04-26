# 탑.py
# Question Link: https://www.acmicpc.net/problem/2493
# Primary idea:     자료구조, 스택
#                   1. 2중 반복문(O(n^2))이여서 시간초과남
# 
# Time Complexity : O() 
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

import sys

N = int(input())
height = list(map(int, sys.stdin.readline().split(' ')))

stack = []
res = [0 for _ in range(N)]

## 시간초과 ##
# reverseHeight = height[::-1]
# for i in range(N):
#     for j in range(i+1, N):
#         if reverseHeight[i] < reverseHeight[j]:
#             res[N - i - 1] = N - j # 해당 탑의 index를 저장
#             break

for i in range(N):
    while stack:
        if stack[-1][0] <= height[i]:
            stack.pop()
        else:
            res[i] = stack[-1][1] + 1
            break

    stack.append([height[i], i]) # 높이, index

print(*res)