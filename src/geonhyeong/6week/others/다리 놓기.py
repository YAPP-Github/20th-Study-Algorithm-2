# 다리 놓기.py
# Question Link: https://www.acmicpc.net/problem/1010
# Primary idea:     DP
#                   1. 
#  
# 참고 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=occidere&logNo=220876138317
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 216 ms
# Memory Usage: 30.840 MB

import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스의 수

for _ in range(T):
    left, right = map(int, input().split())
    dp = [[0 for j in range(31)] for i in range(31)]

    # 제일 위에 있는 곳
    for i in range(1, right+1):
        dp[1][i] = i
    
    for i in range(2, left+1):
        for j in range(i, right+1):
            for k in range(j, i-1, -1):
                dp[i][j] += dp[i-1][k-1]
            
    print(dp[left][right])