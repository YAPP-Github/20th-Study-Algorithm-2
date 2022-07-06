n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

def solution(n, results):
    answer = 0
    players = [[0]* n for _ in range(n)]
    for result in results:
        w, l = result
        players[w-1][l-1] = 1 #이기면 1, 지면 -1
        players[l-1][w-1] = -1

    for i in range(n):
        # i에게 지면, i에게 이긴 애들한테도 짐
        for j in range(n):
            #j가 i에게 진다면, j는 i에게 이긴 애들한테도 진다.
            if players[j][i] == -1:
                for k in range(n):
                    if players[k][i] == 1:
                        players[j][k] = -1
                        players[k][j] = 1
            #j가 i에게 이긴다면, j는 i에게 진애들에게 이긴다
            if players[j][i] == 1:
                for k in range(n):
                    if players[i][k] == 1:
                        players[j][k] = 1
                        players[k][j] = -1

    for player in players:
        if player.count(0) == 1:
            answer += 1
    return answer

print(solution(n,results))