# 공주님을 구해라!.py
# Question Link: https://www.acmicpc.net/problem/17836
# Primary idea:     BFS, 그래프 이론, 그래프 탐색
#                   1. 정형적인 BFS문제 + 구현
#                   2. dx, dy을 미리 선언해 4방향을 바라볼수 있게 한다.
#                   3. 최소값을 찾아야하는 문제이니 int의 최대값을 미리 선언
#                   4. queue를 통해 x, y, time을 저장
#                   5. visited로 방문한적이 있는지 확인
#                   6. 조기 탈출 조건
#                       1) x, y가 N, M에 도달할 경우 -> board의 마지막 위치 = 공주님 위치
#                       2) time이 T에 도달하기 직전
# 
# Time Complexity : O(n^2)
# Space Complexity : O()
# Runtime: 112 ms
# Memory Usage: 32.46 MB

import sys
from collections import deque
input = sys.stdin.readline

# out of boundary
def checkBound(x, y):
    return 0 <= x < N and 0 <= y < M

# 초기 입력
N, M, T = map(int, input().split())

# 선언
board = [[] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
queue = deque() # 입구 입성(x, y), time
queue.append((0, 0, 0))
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
res = float('inf')

# 저장
for i in range(N):
    data = list(map(int, input().split()))
    board[i] = data

while queue:
    x, y, time = queue.popleft()

    # 탈출 1
    if x == N-1 and y == M-1:
        res = min(res, time)
        break

    # 탈출 2
    if time+1 > T: break

    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y

        if not checkBound(nx, ny): continue # out of index
        if visited[nx][ny]: continue # 방문한적이 있는지
        if board[nx][ny] == 1: continue # 벽
        elif board[nx][ny] == 0:
            visited[nx][ny] = 1
            queue.append([nx, ny, time+1])
        else: # 2 성검
            visited[nx][ny] = 1
            getSwordTime = (time+1) + abs(nx-(N-1)) + abs(ny-(M-1))
            if getSwordTime <= T:
                res = getSwordTime

print(res) if res <= T else print("Fail")