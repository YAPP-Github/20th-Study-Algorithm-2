# 빗물.py
# Question Link: https://www.acmicpc.net/problem/14719
# Primary idea:     구현
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 68 ms
# Memory Usage: 30.840 MB

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))

res = 0
for i in range(1, w - 1): # 첫 번째 칸과 마지막칸은 물이 고일수 없음
    leftMax = max(block[:i]) # 기준에서 가장 높은 왼쪽
    rightMax = max(block[i+1:]) # 기준에서 가장 높은 오른쪾

    compare = min(leftMax, rightMax)

    if block[i] < compare:
        res += compare - block[i]

print(res)
