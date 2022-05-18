n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input())))

answer = 0
for case in range(1<<n*m):
    score = 0
    for i in range(n):
        rowScore = 0
        for j in range(m):
            index = i*m+j
            if case & (1<<index) != 0:
                rowScore = rowScore*10 + paper[i][j]
            else:
                score += rowScore
                rowScore = 0
        score += rowScore

    for j in range(m):
        colScore = 0
        for i in range(n):
            index = i*m+j
            if case & (1<<index) == 0:
                colScore = colScore*10 + paper[i][j]
            else:
                score += colScore
                colScore = 0
        score += colScore
    answer = max(answer, score)
print(answer)
