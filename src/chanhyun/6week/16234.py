from collections import deque

n, l, r = map(int, input().split())
population = []
for _ in range(n):
    population.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

find = False
united = [[0]*n for _ in range(n)]
def unite(i, j):
    global find
    countries = [(i, j)]
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            #맵 범위 안에 존재하고
            if nx < n and nx > -1 and ny < n and ny > -1:
                #아직 연합 판정 안했고
                if united[nx][ny] == 0:
                    d = abs(population[nx][ny] - population[x][y])
                    #인구 차이가 적절하고
                    if d >= l and d <= r:
                        find = True
                        united[nx][ny] = united[x][y]
                        q.append((nx, ny))
                        countries.append((nx, ny))
    return countries

def move():
    global find
    count = 1
    for i in range(n):
        for j in range(n):
            if united[i][j] == 0:
                united[i][j] = count
                countries = unite(i,j)
                count += 1
                total_pop = 0
                for c in countries:
                    total_pop += population[c[0]][c[1]]
                avg_pop = total_pop // len(countries)
                for c in countries:
                    population[c[0]][c[1]] = avg_pop
    if find == False:
        return False
    for i in range(n):
        for j in range(n):
            united[i][j] = 0
    return True

days = 0
while True:
    find = False
    if move():
        days += 1
    else:
        break

print(days)
