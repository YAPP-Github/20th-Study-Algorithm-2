# 징검다리 건너기 (large).py
# Question Link: https://www.acmicpc.net/problem/22871
# Primary idea:     이분 탐색, DP
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

import sys
input = sys.stdin.readline

# 시간초과
n = int(input())
A = list(map(int, input().split()))

dp = [0] + [1000000] * (n - 1)

for i in range(1, n):
    for j in range(0, i):
        power = max((i - j) * (1 + abs(A[i] - A[j])), dp[j])
        dp[i] = min(dp[i], power)

print(dp[-1])