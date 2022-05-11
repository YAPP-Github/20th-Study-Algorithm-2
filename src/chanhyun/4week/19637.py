# 이분탐색으로 풀어도 시간초과

import sys
input = sys.stdin.readline

def binary_search(t, p):
    l = 0
    r = len(t)-1
    ptr = 0
    while l<=r:
        mid = (l+r) // 2
        if p <= int(t[mid][1]):
            ptr = mid
            r = mid-1
        elif p > int(t[mid][1]):
            l = mid+1
    return ptr

n, m = map(int, input().split())
title = []
for _ in range(n):
    item = input().split()
    if title and title[-1][1] == item[1]:
        continue
    title.append(item)

for _ in range(m):
    index = binary_search(title, int(input()))
    print(title[index][0])
