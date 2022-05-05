import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] +=1
    while queue:
        v = queue.popleft()
        for w in friends[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                queue.append(w)


n = int(input())
m = int(input())

friends = list([] for _ in range(n+1))
visited = [0] * (n+1)
for i in range(m):
    a,b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

bfs(1)
result = 0
for i in range(2, n+1):
    if (0 < visited[i] <= 3):
        result+=1

print(result)
