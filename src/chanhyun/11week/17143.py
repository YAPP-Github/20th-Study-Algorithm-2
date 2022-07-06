rl, cl, ml = map(int, input().split())
water = [[0 for _ in range(cl)] for _ in range(rl)]
answer = 0
for _ in range(ml):
    r,c,s,d,z = map(int, input().split())
    water[r-1][c-1] = [s,d-1,z]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def catch(pos):
    for i in range(rl):
        if water[i][pos] != 0:
            shark = water[i][pos][2]
            water[i][pos] = 0
            return shark
    return 0

def move():
    temp = [[0 for _ in range(cl)] for _ in range(rl)]
    for i in range(rl):
        for j in range(cl):
            if water[i][j] != 0:
                s, d, z = water[i][j]
                x = i
                y = j
                while s > 0:
                    x += dx[d]
                    y += dy[d]
                    if 0<=x<rl and 0<=y<cl:
                        s -= 1
                    else:
                        x -= dx[d]
                        y -= dy[d]
                        if d==0: d=1
                        elif d==1: d=0
                        elif d==2: d=3
                        elif d==3: d=2
                if temp[x][y] == 0:
                    temp[x][y] = [water[i][j][0],d,z]
                else:
                    if temp[x][y][2] < z:
                        temp[x][y] = [water[i][j][0],d,z]
    return temp

for pos in range(cl):
    answer += catch(pos)
    water = move()

print(answer)
