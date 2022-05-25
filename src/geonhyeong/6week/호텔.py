# 호텔.py
# Question Link: 
# Primary idea:     DP
#                   1. 문재가 이해가 안간다...
#                   2. 문제 Tip
#                       A~D까지의 물건이 있고 각 물건은 가치가 다르며, 배낭의 크기 또한 정해져 있다고 합시다.
#                       그렇다면 최대(혹은 최소)의 가치를 가지도록 물건을 훔치려면
#                       어떤 물건들을 담아야할까요?
#                       
#                       1) 물건을 담는다, 안 담는다 이 두 가지 상태만 존재한다면    -> 0/1 Knapsack         -> Dynamic Programming 
#                       2) 물건을 쪼개어서라도 담을 수 있다면                   -> fractional Knapsack  -> Greedy
#                   3. 
#
# 참고 : https://velog.io/@pjh612/%EB%B0%B1%EC%A4%80-1106%EB%B2%88-%ED%98%B8%ED%85%94
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 1016 ms
# Memory Usage: 34.692 MB

import sys
input = sys.stdin.readline

c, n = map(int, input().split())

dp = [0 for _ in range(1000*100+1)]

for _ in range(n):
    cost, customer = map(int, input().split())

    for i in range(1, 100001):
        if i - cost >= 0:
            dp[i] = max(dp[i], dp[i - cost] + customer)

for i in range(1, 100001):
    if dp[i] >= c:
        print(i)
        break