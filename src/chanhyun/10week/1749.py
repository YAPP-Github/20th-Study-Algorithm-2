import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = (dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]) + graph[i-1][j-1]

answer = -1e9
for x1 in range(1, n+1):
    for y1 in range(1, m+1):
        for x2 in range(x1, n+1):
            for y2 in range(y1, m+1):
                answer = max(answer, dp[x2][y2]-(dp[x1-1][y2]+dp[x2][y1-1]-dp[x1-1][y1-1]))
print(answer)
