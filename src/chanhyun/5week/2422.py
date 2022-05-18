n, m = map(int, input().split())
pairs = [[True for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    pairs[a][b] = False
    pairs[b][a] = False

answer = 0
for i in range(1,n+1):
    for j in range(i+1, n+1):
        for k in range(j+1, n+1):
            if pairs[i][j] and pairs[i][k] and pairs[j][k]:
                answer += 1

print(answer)
