# 블로그.py
# Question Link: https://www.acmicpc.net/problem/21921
# Primary idea:     투 포인터
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 224 ms
# Memory Usage: 59.888 MB

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
numVisitors = list(map(int, input().split()))

sum = 0
sumList = [0] # 첫 계산
for i in numVisitors: # 각 구간(data)에 대하여 누적 합을 계산한 배열(sumList)을 생성
    sum += i # 누적
    sumList.append(sum) # [1, 5, 7, 12, 13]

res = []
for i in range(0, n-x+1):
    res.append(sumList[i+x] - sumList[i])

if max(res) == 0:
    print('SAD')
else:
    print(max(res))
    print(res.count(max(res)))


############### 시간초과 ###############
# res = []
# for i in range(0, n-x+1):
#     res.append(sum(numVisitors[i:i+x]))

# if max(res) == 0:
#     print('SAD')
# else:
#     print(max(res))
#     print(res.count(max(res)))
######################################