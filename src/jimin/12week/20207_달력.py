import sys
input = sys.stdin.readline

n = int(input())
calendar_list = []
calendar = [0] * 366
for i in range(n):
    s, e = map(int, input().split())
    for j in range(s, e+1):
        calendar[j] += 1

max_col, count = 0, 0
answer = 0
for i in range(1,366):
    if calendar[i] == 0:
        answer += max_col * count
        max_col, count = 0, 0
        continue
    max_col = max(max_col, calendar[i])
    count += 1

answer += max_col * count
print(answer)


