def explode(x,y,time):
    board[x][y] = '.'
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + d[0]
        ny = y + d[1]
        if 0<=nx<r and 0<=ny<c:
            if board[nx][ny] != '.' and board[nx][ny]+3 == time:
                continue
            board[nx][ny] = '.'

r, c, n = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))

time = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == 'O':
            board[i][j] = 0

#다음 1초 동안 봄버맨은 아무것도 하지 않는다.
time += 1

while time < n:
    #다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다.
    time += 1
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                board[i][j] = time

    if time >= n:
        break

    #1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
    time += 1
    for i in range(r):
        for j in range(c):
            if board[i][j] != '.' and board[i][j] + 3 == time:
                explode(i,j,time)

for i in range(r):
    for j in range(c):
        if board[i][j] != '.':
            print('O', end='')
        else:
            print('.', end='')
    print()