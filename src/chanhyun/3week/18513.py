import heapq

n, k = map(int, input().split())
sam = list(map(int, input().split()))
visited = set()
unhappiness = 0

q = []
for s in sam:
    heapq.heappush(q, [0, s])
    visited.add(s)

while q and k > 0:
    t, now = heapq.heappop(q)
    for d in [1, -1]:
        if now + d not in visited:
            if k > 0:
                heapq.heappush(q, [t+1, now+d])
                visited.add(now + d)
                unhappiness += t+1
                k -= 1
            else:
                break

print(unhappiness)