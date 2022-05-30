# .py
# Question Link: 
# Primary idea:     String
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
food = [list(map(int, input().split())) for _ in range(n)]
tree = {(i, j): deque() for i in range(n) for j in range(n)}
origin_food = [[5] * n for _ in range(n)]


def outOfboundary(x, y):
    return x < 0 or x >= n or y < 0 or y >= n


for i in range(m):
    x, y, age = list(map(int, input().split()))
    tree[(x - 1, y - 1)].append(age)

for i in range(k):
    # 봄/여름
    for (x, y), ages in tree.items():
        survive = deque()
        sumv = 0    
        for age in ages:
            if origin_food[x][y] >= age:
                origin_food[x][y] -= age
                survive.append(age + 1)
            else:
                sumv += age // 2

        tree[(x, y)] = survive
        origin_food[x][y] += sumv

    # 가을/겨울
    for (x, y), ages in tree.items():
        for age in ages:
            if age % 5 == 0:
                if not outOfboundary(x - 1, y - 1):
                    tree[(x - 1, y - 1)].appendleft(1)

                if not outOfboundary(x - 1, y):
                    tree[(x - 1, y)].appendleft(1)

                if not outOfboundary(x - 1, y + 1):
                    tree[(x - 1, y + 1)].appendleft(1)

                if not outOfboundary(x, y - 1):
                    tree[(x, y - 1)].appendleft(1)

                if not outOfboundary(x, y + 1):
                    tree[(x, y + 1)].appendleft(1)

                if not outOfboundary(x + 1, y - 1):
                    tree[(x + 1, y - 1)].appendleft(1)

                if not outOfboundary(x + 1, y):
                    tree[(x + 1, y)].appendleft(1)

                if not outOfboundary(x + 1, y + 1):
                    tree[(x + 1, y + 1)].appendleft(1)

    for i in range(n):
        for j in range(n):
            origin_food[i][j] += food[i][j]

cnt = 0
for node in tree.values():
    cnt+=len(node)

print(cnt)