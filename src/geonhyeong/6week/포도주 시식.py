# 포도주 시식.py
# Question Link: https://www.acmicpc.net/problem/2156
# Primary idea:     DP
#                   1. 고려사항
#                       1) 현재 포도주와 이전 포도주를 마시고 전전 포두주는 마시지 않는다. ( wine[i]+wine[i-1]+d[i-3] )
#                       2) 현재 포도주와 전전 포도주를 마시고 이전 포도주는 마시지 않는다. ( wine[i]+d[i-2] )
#                       3) 현재 포도주를 마시지 않는다. ( d[i-1] )
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 84 ms
# Memory Usage: 30.840 MB

import sys
input = sys.stdin.readline

n = int(input())
wine = []

for i in range(n):
    wine.append(int(input()))

dp = [0] * n


dp[0] = wine[0]
if n > 1:
    dp[1] = wine[0]+wine[1]

if n > 2:
    dp[2] = max(wine[2] + wine[1], wine[2] + wine[0], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])

print(dp[n-1])