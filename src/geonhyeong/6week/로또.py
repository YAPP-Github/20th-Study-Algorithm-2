# 로또.py
# Question Link: https://www.acmicpc.net/problem/2758
# Primary idea:     DP
#                   1. 
# 
# 참고 : https://boomrabbit.tistory.com/36
# Time Complexity : O(n * m)
# Space Complexity : O()
# Runtime: 1708 ms
# Memory Usage: 30.840 MB

import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스의 수

for _ in range(T):
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, m+1):
        dp[1][i] = i
    
    for i in range(2, n+1):
        for j in range(2, m+1):
            # i번째 숫자로 j를 선택하는 경우 + 선택하지 않는 경우
            dp[i][j] = dp[i-1][j//2] + dp[i][j-1]

    for i in range(1, n+1):
        print(dp[i], sep= " ")

    print(dp[n][m])