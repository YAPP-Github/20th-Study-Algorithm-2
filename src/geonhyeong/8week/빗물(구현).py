# 빗물.py
# Question Link: https://www.acmicpc.net/problem/14719
# Primary idea:     구현
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))

res = 0
for i in range(1, w - 1):
    leftMax = max(block[:i])
    rightMax = max(block[i+1:])

    compare = min(leftMax, rightMax)

    if block[i] < compare:
        res += compare - block[i]

print(res)
