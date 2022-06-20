import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

count = 0
while len(cards) >= 2:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    count += a+b
    heapq.heappush(cards, count)

print(count)