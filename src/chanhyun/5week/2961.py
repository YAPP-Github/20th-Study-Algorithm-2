n = int(input())
sb = []
for _ in range(n):
    sb.append(list(map(int, input().split())))

answer = 1000000000
for i in range(1, 1<<n):
    sour = 1
    bitter = 0
    for j in range(n):
        if i & (1<<j) != 0:
            sour *= sb[j][0]
            bitter += sb[j][1]
    answer = min(answer, abs(sour-bitter))
print(answer)