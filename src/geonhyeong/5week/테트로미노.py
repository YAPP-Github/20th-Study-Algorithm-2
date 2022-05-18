# 테트로미노.py
# Question Link: https://www.acmicpc.net/problem/14500
# Primary idea:     완전 탐색
#                   1. 회전이나 대칭을 생각해야한다 -> 작좁 규횬운 굉장히 구현적으로 시간이 많이 걸린다
#                   2. dfs로 depth를 생각하며 구한다.
#                       1) 'ㅜ'를 제외한 모양은 모두 depth 0~3
#                       2) 'ㅜ'는 사용한 갯수(cnt)가 1일때 새로운 블록에서 다음 블록을 탐색하는 것이 아닌 '기존 블록에서 탑색'
#                   3. 시간초과 문제로 미리 최댓값을 계산 해야한다.
#                       1) 배열에서 가장 큰 값을 미리 구한다.
#                       2) 탐색전, '누적값 + 최댓값 * 탐색해야하는 남은 갯수'를 했을떄도 최종 값보다 작으면 return
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 272 ms
# Memory Usage: 37.59 MB

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []

# 입력
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
isVisited = [[False for _ in range(M)] for _ in range(N)]
res = 0
maxValue = max(map(max, board))

def dfs(x, y, cnt, sum):
    global res

    # 탐색전, '누적값 + 최댓값 * 탐색해야하는 남은 갯수'를 했을떄도 최종 값보다 작으면 return
    if res >= sum + maxValue * (3 - cnt):
        return

    # 4개의 블록을 모두 사용할 경우
    if cnt == 3:
        res = max(res, sum)
        return
    
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        # out of boundary, 방문을 안했는지
        if 0 <= nx < N and 0 <= ny < M and not isVisited[nx][ny]:
            if cnt == 1: # ㅜ 모양, depth를 '기존 block'에서 탐색
                isVisited[nx][ny] = True
                dfs(x, y, cnt+1, sum + board[nx][ny])
                isVisited[nx][ny] = False
            isVisited[nx][ny] = True
            dfs(nx, ny, cnt+1, sum + board[nx][ny])
            isVisited[nx][ny] = False

for x in range(N):
    for y in range(M):
        isVisited[x][y] = True
        dfs(x, y, 0, board[x][y])
        isVisited[x][y] = False

print(res)