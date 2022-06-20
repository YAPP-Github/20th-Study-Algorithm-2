n = int(input())
problems = list(input())

blue = 0
red = 0
if problems[0] == 'B':
    blue += 1
else:
    red += 1

for i in range(1, n):
    if problems[i-1] != problems[i]:
        if problems[i] == 'B':
            blue += 1
        else:
            red += 1

print(1+min(blue, red))
