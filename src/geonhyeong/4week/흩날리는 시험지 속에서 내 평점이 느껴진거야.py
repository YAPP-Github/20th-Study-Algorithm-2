# 흩날리는 시험지 속에서 내 평점이 느껴진거야.py
# Question Link: https://www.acmicpc.net/problem/17951
# Primary idea:     String, 정렬
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
solution = list(map(int,input().split())) 

left, right = 0, sum(solution)+1 # right = 최댓값

while left + 1 < right:
    mid = (left + right) // 2
    cnt = 0
    sum = 0
    
    for i in range(0, N):
        sum += solution[i] # 각 시험지의 점수를 더하고
        if sum >= mid: # 설정한 기준 점수보다 sum값이 커지면 그룹을 분리함
            sum = 0
            cnt += 1 # 그룹 개수 카운트

    if cnt >= K:
        left = mid
    else:
        right = mid # 카운트한 그룹 개수가 k보다 작으면 기준 점수를 낮춰서 그룹의 개수를 더 많이 생성하는 범위로 좁힘

print(left)