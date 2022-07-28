def solution(n, results):
    answer = 0
    table = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for r in results:
        table[r[0]][r[1]] = 1   #승
        table[r[1]][r[0]] = -1   #패
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j or table[i][j] != 0:
                    continue
                if table[i][k] == 1 and table[k][j] == 1:
                    table[i][j] = 1
                    table[j][i] = -1
                    table[k][i] = -1
                    table[j][k] = -1
    for t in table:
        if t.count(0) == 2:
            answer += 1
    return answer