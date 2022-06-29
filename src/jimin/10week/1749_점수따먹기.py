#1749 점수 따먹기
import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
arr =[list(map(int,input().split())) for _ in range(n)]
prefix_sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        prefix_sum[i+1][j+1] = arr[i][j] + prefix_sum[i][j+1] + prefix_sum[i+1][j] - prefix_sum[i][j]

max_sum = -math.inf
for i in range(1, n+1):
    for j in range(1, m+1): #시작 점
        for k in range(i, n+1):
            for l in range(j, m+1): #종료 점
                max_sum = max(max_sum, prefix_sum[k][l] - prefix_sum[i-1][l] - prefix_sum[k][j-1] + prefix_sum[i-1][j-1])

print(max_sum)