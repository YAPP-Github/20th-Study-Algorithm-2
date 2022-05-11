# IF문 좀 대신 써줘.py
# Question Link: https://www.acmicpc.net/problem/19637
# Primary idea:     String, 정렬
#                   1. value를 list로 가지는 dictionary
#                      : 같은 전투력을 가진 칭호가 여러개 있을 수 있어서 list
#                   2. 전투력 리스트 - 이분탐색을 위해 시작, 중간, 끝을 찾아주기 위해 사용
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

import sys
from collections import defaultdict
input = sys.stdin.readline

def binarySearch(p):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start+end) // 2

        if p == power[mid]:
            return standard[power[mid]]
        elif p < power[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return standard[power[start]]

N, M = map(int, input().split()) # 칭호의 개수, 캐릭터들의 개수
standard = defaultdict(list)
power = []

# 저장
for _ in range(N):
    name, p = input().split()
    standard[int(p)].append(name) # 먼저 들어온 칭호부터
    power.append(int(p))

for _ in range(M):
    p = int(input())
    res = binarySearch(p)
    print(res[0])