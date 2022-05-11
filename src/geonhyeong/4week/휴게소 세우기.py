# 휴게소 세우기.py
# Question Link: https://www.acmicpc.net/problem/1477
# Primary idea:     String, 정렬
#                   1. 입력을 받으면서 휴게소 배열(arr)의 양 끝에 출발지점과 도착지점을 추가해주고 정렬
#                   2. start, end는 휴게소 위치의 범위
#                   3. 이분탐색
#                       - mid : 가장 멀리 떨어져 있는 휴게소 사이 거리
#                       - cnt : 설치해야 할 휴게소 개수
#                       - 모든 거리를 완전 탐색을 해서 mid보다 큰 경우, 해당 mid로 나누어서 설치해야 할 휴게소 개수를 구한다.
#                       - 설치해야 할 휴게소 개수가 M보다 크다면 mid는 더 길어야 한다.
#                       - 설치해야 할 휴게소 개수가 M보다 작다면 mid는 더 짧아야 한다. (조건 만족은 했으므로 result = mid)
#                   4. result 출력
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