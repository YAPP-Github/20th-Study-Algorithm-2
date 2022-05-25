# 인구 이동.py
# Question Link: https://www.acmicpc.net/problem/16234
# Primary idea:     dp
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

import sys
from collections import deque
input = sys.stdin.readline


N, L, R = map(int, input().split())
countries = [] # 각 나라의 인구수

# input
for _ in range(N):
    cols = list(map(int, input().split()))
    countries.append(cols)

# init
res = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def outOfIndex(x, y):
    return not (0 <= x < N and 0 <= y < N)

def is_union(base, other):
    return (L <= abs(base - other) <= R)

def bfs(x, y):
    visited = [(x, y)]
    queue = deque([(x, y)])
    sum = 0 # 연합한 나라의 누적값
    cnt = 0 # 연합한 나라의 갯수

    while queue:
        x, y = queue.popleft()
        sum += countries[x][y]  # 나라의 인구 누적
        cnt += 1                # 나라의 갯수 증가
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if outOfIndex(nx, ny): continue
            if (nx, ny) in visited: continue
            if is_union(countries[x][y], countries[nx][ny]):
                queue.append((nx, ny))
                visited.append((nx, ny))
    
    return sum // cnt, visited

def fill_in_countries(total, visited):
    for x, y in visited:
        countries[x][y] = total

cnt = 0
not_visited = []

while True:
    break_flag = False
    visited = []
    fill_list = []
    for i in range(N):
        for j in range(N):
            if (i, j) in visited: continue
            total, union_visited = bfs(i, j)
            visited += union_visited
            fill_list.append((total, union_visited))
            
            if len(union_visited) > 1:
                break_flag = True

    for total, union_visited in fill_list:
        fill_in_countries(total, union_visited)

    if not break_flag:
        break
    cnt += 1

print(cnt)
