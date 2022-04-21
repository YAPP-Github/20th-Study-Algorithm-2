n = int(input())
towers = list(map(int, input().split()))
answer = []

dic = dict()
dic[0] = 0
for i in range(n):
    dic[towers[i]] = i+1

for _ in range(n):
    temp = []
    now = towers.pop()

    while towers and now > towers[-1]:
        temp.append(towers.pop())
    if towers:
        answer.append(towers[-1])
    else:
        answer.append(0)

    while temp:
        towers.append(temp.pop())

answer.reverse()
for a in answer:
    print(dic[a], end=' ')