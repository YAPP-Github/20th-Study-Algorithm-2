# 치킨 배달.py
# Question Link: https://www.acmicpc.net/problem/15686
# Primary idea:     완전 탐색
#                   1. 잡(1), 치킨(2)에 대한 좌표값을 저장
#                   2. 치킨집을 M개 선택했을 떄의 '모든 조합'을 구한다
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 712 ms
# Memory Usage: 30.84 MB

import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
houseList = []
chichkenList = []

# 입력
for i in range(N):
    for (j, value) in enumerate(list(map(int, input().split()))):
        if value == 1: # 집
            houseList.append([i+1, j+1])
        elif value == 2: # 치킨
            chichkenList.append([i+1, j+1])

minDistance = float('inf')

# 치킨집 조합에 따른 집과의 거리        
for combi in combinations(chichkenList, M):
    distance = 0                    # 도시의 치킨 거리
    for house in houseList:
        chichenDist = float('inf')  # 각 집마다 치킨 거리
        for chichen in combi:
            chichenDist = min(chichenDist, abs(house[0] - chichen[0]) + abs(house[1] - chichen[1]))
        distance += chichenDist
        
    minDistance = min(minDistance, distance)

print(minDistance)

