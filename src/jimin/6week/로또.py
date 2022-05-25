#2758 로또
#1부터 m까지 n개의 수 고름
#이전에 고른 수보다 적어도 2배가 되도록 고른다

import sys
input = sys.stdin.readline

t = int(input())
arr = []
for i in range(t):
    n,m = map(int, input().split()) #m중 n개

    dp = list([0] * 2001 for _ in range(11)) # m <= 2000, n <= 10

    for i in range(1, 2001):
        dp[1][i] = i #1개를 뽑는 경우, 본인 수 만큼

    for i in range(2,n+1):
        for j in range(2,m+1):
            #i포함하지 않는 경우 + i포함한 경우 (i//2까지 수 중에서 j-1개)
            dp[i][j] = dp[i][j-1]+dp[i-1][j//2]

    print(dp[n][m])