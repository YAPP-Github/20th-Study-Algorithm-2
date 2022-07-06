answer = 1e9
def isNext(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

def dfs(now, target, words, visited, count):
    global answer
    if now == target:
        answer = min(answer, count)
        return
    for i in range(len(words)):
        if not visited[i] and isNext(now, words[i]):
            visited[i] = True
            dfs(words[i], target, words, visited, count+1)
            visited[i] = False

def solution(begin, target, words):
    visited = [False for _ in range(len(words))]
    dfs(begin, target, words, visited, 0)
    if answer == 1e9:
        return 0
    else:
        return answer