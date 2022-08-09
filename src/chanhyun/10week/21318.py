import sys
input = sys.stdin.readline

n = int(input())
level = list(map(int, input().split()))

dp = [0 for _ in range(n)]
for i in range(1, n):
    if level[i-1] > level[i]:
        dp[i] = dp[i-1]+1
    else:
        dp[i] = dp[i-1]

q = int(input())
for _ in range(q):
    s, e = map(int, input().split())
    print(dp[e-1]-dp[s-1])
