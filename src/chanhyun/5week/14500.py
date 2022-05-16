def rotate(t):
    n = len(t)
    m = len(t[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = t[i][j]
    return result

def horizontal_symmetry(t):
    n = len(t)
    m = len(t[0])
    result = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][m-1-j] = t[i][j]
    return result

def vertical_symmetry(t):
    n = len(t)
    m = len(t[0])
    result = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[n-1-i][j] = t[i][j]
    return result

def move(b, t):
    max_score = 0
    for x in range(len(b)-len(t)+1):
        for y in range(len(b[0])-len(t[0])+1):
            max_score = max(max_score, getScore(x, y, b, t))
    return max_score

def getScore(x, y, b, t):
    score = 0
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] == 1:
                score += b[x+i][y+j]
    return score

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

tet1 = [[1, 1, 1, 1]]
tet2 = [[1, 1],
        [1, 1]]
tet3 = [[1, 0],
        [1, 0],
        [1, 1]]
tet4 = [[1, 0],
        [1, 1],
        [0, 1]]
tet5 = [[1, 1, 1],
        [0, 1, 0]]
tetlist = [tet1, tet2, tet3, tet4, tet5]

answer = 0
for tet in tetlist:
    for i in range(4):
        tet = rotate(tet)
        answer = max(answer, move(board, tet))
        sym = horizontal_symmetry(tet)
        answer = max(answer, move(board, sym))
        sym = vertical_symmetry(tet)
        answer = max(answer, move(board, sym))

print(answer)
