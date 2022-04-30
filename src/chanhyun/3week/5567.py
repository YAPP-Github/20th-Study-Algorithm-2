from collections import deque

n = int(input())
m = int(input())
friend = [[] for _ in range(501)]
for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

q = deque([])
visited = [False for _ in range(501)]
cnt = 0
if len(friend[1]) != 0:
    q.append([1,0])
    visited[1] = True
    while q:
        x, d = q.popleft()
        for y in friend[x]:
            if not visited[y]:
                if d < 2:
                    visited[y] = True
                    q.append([y, d+1])
                    cnt += 1
print(cnt)
