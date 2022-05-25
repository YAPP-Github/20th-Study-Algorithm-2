# 돌 게임.py
# Question Link: https://www.acmicpc.net/problem/9655
# Primary idea:     DP
#                   1. N의 짝 홀수 판단을 이용한 풀이 -> N이 홀수이면 상근이의 승, 짝수면 창용이의 승
#                   2. 다이나믹 프로그래밍(DP)을 이용한 풀이 -> 게임과정의 횟수
#                       : DP[N] = min ( (DP[N - 1] + 1의 경우) OR (DP[N - 3] + 1의 경우) )
#                       : 홀수면 상근이의 승, 짝수면 창용이의 승
# 
# 참고 : https://beginnerdeveloper-lit.tistory.com/83
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 68 ms
# Memory Usage: 30.840 MB

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 1001 # 게임 횟수
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = min(dp[i-1]+1, dp[i-3]+1)

if dp[n] % 2 == 1:
    print("SK")
else:
    print("CY")