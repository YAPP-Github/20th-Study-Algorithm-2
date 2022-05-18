#15686 치킨 배달
import sys
import math
input = sys.stdin.readline
from itertools import combinations

n,m = map(int, input().split()) #n x n 크기 도시, 최대 치킨 집
arr = [list(map(int,input().split())) for _ in range(n)]

houses = []
chicken = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            houses.append([i,j])
        elif arr[i][j] == 2:
            chicken.append([i,j])

result_dist = math.inf
for c in combinations(chicken, m): #치킨집 후보들
    sub_dist = 0
    for x,y in houses: #집 하나에서 가장 가까운 치킨집 찾고 모든 집에 대해 부분 합
        min_dist = math.inf
        for i in range(m):
            min_dist = min(abs(c[i][0]-x) + abs(c[i][1]-y), min_dist)
        sub_dist += min_dist
    result_dist = min(result_dist, sub_dist)

print(result_dist)