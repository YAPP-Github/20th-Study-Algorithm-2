c, n = map(int, input().split())
cities = []
for _ in range(n):
    cities.append(list(map(int, input().split())))
cities.sort(key=lambda x: x[0])

dp = [1e9 for _ in range(c+101)]
dp[0] = 0
for cost, customer in cities:
    for i in range(customer, c+101):
        dp[i] = min(dp[i-customer]+cost, dp[i])

print(min(dp[c:]))
