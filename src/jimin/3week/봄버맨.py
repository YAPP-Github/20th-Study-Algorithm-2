import sys
from collections import deque
input = sys.stdin.readline

#1. 최초 폭탄 존재
#2. 1초는 가만히
#3. 2초된다면 모든 칸에 폭탄 설치
#4. 3초가 된다면 모두 폭발
#3,4 반복

#rxc 크기, n초
r,c,n = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def set_bomb():
    bombs = []
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '.':
                arr[i][j] = "O"
            elif arr[i][j] == 'O':
                bombs.append([i, j])
    return bombs


def find_bomb(): #폭발 장소 저장
    bombs = []
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'O':
                bombs.append([i,j])

    return bombs

def bfs(y,x): #폭발
    queue = deque()
    queue.append([y,x])
    while queue:
        y,x = queue.popleft()
        arr[y][x] = '.'
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (0 <= ny < r and 0 <= nx < c):
                arr[ny][nx] = '.'

def bomberman(time, bombs):
    if time > n:
        return
    if(time % 2 == 0): #짝수, 폭탄 채운다.
        bombs = set_bomb()
    elif(time %2 == 1): #홀수, 폭발
        for y,x in bombs:
            bfs(y,x)

    bomberman(time+1, bombs)

bombs = find_bomb()
bomberman(2, bombs)

for i in range(r):
    for j in range(c):
        print(arr[i][j], end="")
    print()
