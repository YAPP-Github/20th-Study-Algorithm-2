#16236 아기 상어
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input()) #공간의 크기
arr =[list(map(int,input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(y,x):
    queue = []
    heappush(queue, (0, y, x))
    arr[y][x] = 0
    visited = list([0] * n for _ in range(n))
    visited[y][x] = 1
    size, count, result_time = 2, 0, 0  #현재 사이즈, 먹은 개수, 전체 시간

    while(queue):
        time, y, x = heappop(queue)
        if (0< arr[y][x] <size): # 본인보다 작을때 먹는다..
            count +=1
            arr[y][x] = 0
            if (size == count):
                size += 1
                count = 0
            result_time += time
            time = 0
            visited = list([0] * n for _ in range(n))
            queue = []

        for i in range(4):
            ny, nx = dy[i] + y, dx[i] + x
            if 0 <= ny and ny < n  and 0 <= nx and nx < n and visited[ny][nx] == 0 and arr[ny][nx] <= size:
                heappush(queue, (time+1, ny, nx))
                visited[ny][nx] = 1

    return result_time


#아기 상어 위치 저장
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            y,x = i,j
            break

print(bfs(y,x))