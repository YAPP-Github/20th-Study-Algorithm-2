import copy

n = int(input())
towers = list(map(int, input().split()))
answer = copy.deepcopy(towers)
dict = dict()

idx = n
temp = []
while towers:
    temp.append(towers.pop())
    dict[temp[-1]] = 0
    idx -= 1

    while towers and towers[-1] < temp[-1]:
        temp.append(towers.pop())
        dict[temp[-1]] = 0
        idx -= 1

    if towers:
        while temp and towers[-1] > temp[-1]:
            dict[temp[-1]] = idx
            temp.pop()

for i in range(n):
    print(dict[answer[i]], end=' ')