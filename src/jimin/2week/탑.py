import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int ,input().split()))
result = [0 for _ in range(n)]

for i in range(1, n):
    pre_top = i- 1
    while (pre_top >= 0):
        if (tops[pre_top] > tops[i]):
            result[i] = pre_top + 1
            break
        else:
            pre_top = result[pre_top] - 1

print(*result)