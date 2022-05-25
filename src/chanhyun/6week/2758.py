t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, m+1):
        dp[1][i] = 1
    
    for i in range(2, n+1):
        cnt = 0
        for j in range(2**(i-1), m+1):
            if j % 2 == 0:
                cnt += dp[i-1][j//2]
            dp[i][j] = cnt
    
    print(sum(dp[-1]))