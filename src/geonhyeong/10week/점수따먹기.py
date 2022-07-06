# 점수따먹기.py
# Question Link: https://www.acmicpc.net/problem/1749
# Primary idea:     누적 합
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 4416 ms
# Memory Usage: 116.088 MB

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 행렬 입력받기
arr = [list(map(int,input().split())) for _ in range(n)]

# 누적합 행렬 초기화
sum = [[0] * (m + 1) for _ in range(n + 1)]
 
# 누적합 저장
for i in range(1, n+1):
    for j in range(1, m+1):
        sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + arr[i-1][j-1]

result = -float('inf')

# 최대 누적합 찾기(부분 행렬 구하기)/ 범위 주의!!
for I in range(1, n+1):
    for J in range(1, m+1):
        for i in range(I, n+1):
            for j in range(J, m+1):
                result = max(result, sum[i][j] - sum[i][J-1] - sum[I-1][j] + sum[I-1][J-1])

print(result)