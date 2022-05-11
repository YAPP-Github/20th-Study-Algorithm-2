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

N, M, L = map(int, input().split())
rest = list(map(int, input().split()))
rest.append(0)
rest.append(L)
rest.sort()

left, right = 1, L-1
res = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in range(1, len(rest)):
        # 현재 거리 중 mid보다 큰 거리를 찾아서
        if rest[i]-rest[i-1] > mid:
            # 나눈 만큼 휴게소를 설치 (현재 설치 되어있는 구역은 제외해야해서 -1)
            cnt += (rest[i] - rest[i-1] - 1) // mid
    
    if cnt > M:
        left = mid+1
    else:
        right = mid-1
        res = mid

print(res)