#16234 인구 이동
#국경선을 공유하는 두 나라의 인구 차이가 L <= abs(A[][] - A[][]) <= R, 국경선 연다 -> 열렸다면 이동 시작
#인접한 칸만 이동 가능

import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
arr =[list(map(int,input().split())) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    visited[y][x] = True
    flag = False
    temp = []
    temp.append((y,x))
    while(queue):
        y,x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if l <= abs(arr[y][x] - arr[ny][nx]) <= r: #경계 없어짐
                    flag = True
                    visited[ny][nx] = True
                    queue.append((ny,nx))
                    temp.append((ny, nx))

    if flag:
        get_average(temp)

    return flag


def get_average(temp):
    total_sum = 0
    for y, x in temp:
        total_sum += arr[y][x]
    avg = total_sum // len(temp)
    for y, x in temp:
        arr[y][x] = avg

day = 0
while (1):
    result = False
    visited = list([False] * n for _ in range(n))
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j):
                    result = True

    if (result == False):
        break
    day += 1

print(day)