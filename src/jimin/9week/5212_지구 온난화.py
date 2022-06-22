import sys
import copy
from collections import deque
input = sys.stdin.readline

r,c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

arr_temp = copy.deepcopy(arr)
def bfs():
    global left_i, left_j, right_i, right_j
    queue = deque(X_list)
    while (queue):
        y,x = queue.popleft()
        count_sea = 0
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ( 0 <= ny < r and 0 <= nx < c):
                if ( arr_temp[ny][nx] == "."):
                    count_sea += 1
            else:
                count_sea += 1
        if (count_sea >= 3):
            arr[y][x] = "."
        else:
            left_i, left_j = min(left_i, y), min(left_j, x)
            right_i, right_j = max(right_i, y), max(right_j, x)

left_i, left_j  = r, c
right_i, right_j = -1, -1

X_list = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == "X":
            X_list.append((i,j))

bfs()

for i in range(left_i, right_i+1):
    for j in range(left_j, right_j+1):
        print(arr[i][j], end='')
    print()


