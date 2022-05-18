#2961 도영이가 만든 맛있는 음식

import sys
import math
from itertools import combinations
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    s,b = map(int, input().split())
    arr.append((s,b))

#신맛: 곱, 쓴맛: 합
answer = math.inf
for i in range(1, n+1):
    for c in combinations(arr, i):
        sub_s, sub_b = 1, 0
        for s,b in c:
            sub_s *= s
            sub_b += b
        answer = min(abs(sub_s-sub_b), answer)

print(answer)