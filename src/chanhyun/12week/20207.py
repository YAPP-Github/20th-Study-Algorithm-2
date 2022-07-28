n = int(input())
calendar = [0 for _ in range(366)]
for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        calendar[i] += 1

max_x=0
max_y=0
answer = 0
for i in range(1, 366):
    if calendar[i] == 0:
        answer += max_x*max_y
        max_x = 0
        max_y = 0
    else:
        max_x += 1
        if calendar[i] > max_y:
            max_y = calendar[i]

if max_x != 0:
    answer += max_x*max_y

print(answer)
