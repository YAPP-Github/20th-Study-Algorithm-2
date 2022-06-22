# 카드 정ㅕ하기.py
# Question Link: https://www.acmicpc.net/problem/1715
# Primary idea:     그리디
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 232 ms
# Memory Usage: 33.972 MB

import sys
import heapq 
input = sys.stdin.readline

N = int(input())    # 카드 수
heap = []           # 최소힙
answer = []         # 결과

# 입력
for _ in range(N):
    card = int(input())
    heapq.heappush(heap, card)  # 최소힙

while len(heap) > 1:            # 2개 이상
    A = heapq.heappop(heap)     # 가장 작은 수
    B = heapq.heappop(heap)     # 두번째로 가장 작은 수

    answer.append(A+B)
    heapq.heappush(heap, A+B)

print(sum(answer))