#16235 나무 재테크

import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split()) #nxn 크기, m개의 나무 심음, k년 후에 나무 개수
arr =[list(map(int,input().split())) for _ in range(n)] #겨울에 추가될 양분의 양
dy = [0, 0, -1, 1, 1, -1, 1, -1]
dx = [-1, 1, 0, 0, 1, -1, -1, 1]
food = [[5] * n for _ in range(n)] #현재 양분 저장
trees = [[deque() for _ in range(n)] for _ in range(n)]

for i in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z) #나이 어린 나무부터 양분 먹음, 나이 순으로 정렬되도록

def spring_and_summer():
    # 봄: 나무가 자신의 나이만큼 양분을 먹고 나이 1 증가, 나이 어린 나무부터 양분 먹음 -> age == 양분 만큼 먹어야 함
    for i in range(n):
        for j in range(n):
            tree_cnt = len(trees[i][j])
            for k in range(tree_cnt):
                if trees[i][j][k] <= food[i][j]:
                    food[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    # 여름: 봄에 죽은 나무 양분으로, 나무//2 추가
                    for l in range(k, tree_cnt):
                        food[i][j] += trees[i][j].pop()//2
                    break

def fall_and_winter():
    # 가을: 번식, 나이가 5의 배수만, 인접한 8개에 나이가 1인 나무 생김
    # 겨울: 양분 추가
    for i in range(n):
        for j in range(n):
            tree_cnt = len(trees[i][j])
            for k in range(tree_cnt):
                if trees[i][j][k] % 5 == 0:
                    for l in range(8):
                        nx, ny = i + dx[l], j + dy[l]
                        if (0 <= ny < n and 0 <= nx < n):
                            trees[nx][ny].appendleft(1)

            food[i][j] += arr[i][j]

for i in range(k):
    spring_and_summer()
    fall_and_winter()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)