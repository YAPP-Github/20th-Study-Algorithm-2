# 샘터.py
# Question Link: https://www.acmicpc.net/problem/18513
# Primary idea:     그래프 이론, 그래프 탐색
#                   1. 조합문제 인가?
#                   2. hint를 찾아봄, queue에 (초기 위치, 0)을 초기화 시켜줌
# 
# Time Complexity : O(n^2)
# Space Complexity : O()
# Runtime: 316 ms
# Memory Usage:	56.28 MB

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
water = map(int, input().split())

visited = dict()
queue = deque()

for i in water:
    queue.append(i)
    visited[i] = 0

while queue:
    if K <= 0: break
    i = queue.popleft()

    for j in [i-1, i+1]:
        if j not in visited and K > 0:
            visited[j] = visited[i] + 1
            queue.append(j)
            K -= 1
res = 0
for i, misfortune in visited.items():
    res += misfortune

print(res)