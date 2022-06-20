import sys
import heapq
input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    classes.append(list(map(int, input().split())))
classes.sort()

room = []
time = 0
heapq.heappush(room, classes[0][1])
for i in range(1, n):
    s, t = classes[i][0], classes[i][1]
    time = s
    if time >= room[0]:
        heapq.heappop(room)
    heapq.heappush(room, t)

print(len(room))