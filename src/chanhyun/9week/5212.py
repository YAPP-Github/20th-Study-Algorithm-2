r, c = map(int, input().split())
map = []
for _ in range(r):
    map.append(list(input()))

sink = []
for i in range(r):
    for j in range(c):
        if map[i][j] == 'X':
            count = 0
            for d in [[1,0],[-1,0],[0,1],[0,-1]]:
                ni = i + d[0]
                nj = j + d[1]
                if ni >= r or ni < 0 or nj >= c or nj < 0:
                    count += 1
                elif map[ni][nj] == '.':
                    count += 1
            if count >= 3:
                sink.append((i,j))

for s in sink:
    map[s[0]][s[1]] = '.'

min_i = r
min_j = c
max_i = -1
max_j = -1
for i in range(r):
    for j in range(c):
        if map[i][j] == 'X':
            min_i = min(min_i, i)
            min_j = min(min_j, j)
            max_i = max(max_i, i)
            max_j = max(max_j, j)

later = []
for i in range(min_i, max_i+1):
    later.append(map[i][min_j:max_j+1])

for i in range(len(later)):
    for j in range(len(later[0])):
        print(later[i][j], end='')
    print()