from sys import maxsize


c,n = map(int,input().split())
#얻어야하는 수익, 도시의 갯수

costList =[]
for i in range(n):
    cost, customer = map(int,input().split())
    costList.append((cost,customer))

dp = [maxsize] *(c+100) #제일큰값으로 이뤄진 배열이 최소 c+100만큼
dp[0]=0

minCost = [0]
for cost, customer in costList:
    for i in range(customer, c+100):
        dp[i] = min(dp[i-customer]+cost, dp[i])

print(min(dp[c:])) #c부터 있는 가장 작은 값
