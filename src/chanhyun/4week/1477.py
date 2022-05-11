#19번 라인에서 -1 하는 이유?

import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
rest = list(map(int, input().split()))
rest.append(0)
rest.append(l-1)
rest.sort()

s = 0
e = l-1
while s<=e:
    mid = (s+e)//2
    cnt = 0
    for i in range(1, len(rest)):
        if rest[i]-rest[i-1] > mid:
            cnt += (rest[i]-rest[i-1]-1)//mid
    if cnt > m:
        s = mid+1
    else:
        print('cnt = ', cnt)
        answer = mid
        print(answer)
        e = mid-1

print(answer)
