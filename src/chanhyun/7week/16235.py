n, m, k = map(int, input().split())
ground = [[5 for _ in range(n)] for _ in range(n)]
nutrition = []
for _ in range(n):
    nutrition.append(list(map(int, input().split())))
tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

def springAndSummer():
    for i in range(n):
        for j in range(n):
            dead = []
            tree[i][j].sort()
            for p in range(len(tree[i][j])):
                if ground[i][j] >= tree[i][j][p]:
                    ground[i][j] -= tree[i][j][p]
                    tree[i][j][p] += 1
                else:
                    dead = tree[i][j][p:]
                    tree[i][j] = tree[i][j][:p]
                    break
            for d in dead:
                ground[i][j] += d//2

def fall():
    for i in range(n):
        for j in range(n):
            for p in range(len(tree[i][j])):
                if tree[i][j][p] % 5 == 0:
                    x, y = i, j
                    for d in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                        nx = x + d[0]
                        ny = y + d[1]
                        if 0<=nx<n and 0<=ny<n:
                            tree[nx][ny].append(1)

def winter():
    for i in range(n):
        for j in range(n):
            ground[i][j] += nutrition[i][j]

for _ in range(k):
    springAndSummer()
    fall()
    winter()

count = 0
for i in range(n):
    for j in range(n):
        if tree[i][j] != []:
            count += len(tree[i][j])
print(count)
