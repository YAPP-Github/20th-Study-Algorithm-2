def getRemoveIndex():
    temp = []
    for i in range(101):
        if frame[i]:
            temp.append([count[i],order[i],i])
    temp.sort()
    return temp[0][2]

N = int(input())
total = int(input())
recommend = list(map(int, input().split()))

frame = [False for _ in range(101)]
count = [0 for _ in range(101)]
order = [-1 for _ in range(101)]
frame_count = 0
for i in range(len(recommend)):
    r = recommend[i]
    if frame[r]:
        count[r] += 1
    else:
        if frame_count == N:
            index = getRemoveIndex()
            frame[index] = False
            count[index] = 0
            order[index] = -1
        else:
            frame_count += 1
        frame[r] = True
        count[r] = 1
        order[r] = i

answer = []
for i in range(101):
    if frame[i]:
        print(i, end=' ')