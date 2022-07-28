def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(len(triangle[i])):
            dp[i][j] = triangle[i][j]
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif j == len(triangle[i])-1:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
    for i in range(n):
        for j in range(n):
            answer = max(answer, dp[i][j])
    return answer