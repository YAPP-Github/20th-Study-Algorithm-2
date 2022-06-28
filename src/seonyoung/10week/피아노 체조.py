n= int(input())
msList = list(map(int, input().split()))
m  = int(input())

dp = [0]*n
for i in range(n):
    dp[i]=dp[i-1]
    if msList[i]< msList[i-1]:
        dp[i]+=1
    

for i in range(m):
    start,end = map(int,input().split())
    count = end-start
    print(dp[end-1]-dp[start-1])

