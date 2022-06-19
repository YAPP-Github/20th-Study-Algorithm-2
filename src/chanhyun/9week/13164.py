n, k = map(int, input().split())
heights = list(map(int, input().split()))

differences = [[0,0] for _ in range(n-1)]
for i in range(n-1):
    differences[i][0] = heights[i+1]-heights[i]
    differences[i][1] = i
differences.sort()

separate = []
for i in range(k-1):
    separate.append(differences[n-2-i][1])
separate.sort()

cost = 0
start = 0
for i in range(k-1):
    cost += heights[separate[i]] - heights[start]
    start = separate[i]+1
cost += heights[-1] - heights[start]

print(cost)