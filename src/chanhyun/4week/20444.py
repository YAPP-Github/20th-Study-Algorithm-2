n, k = map(int, input().split())

answer = False
s = 0
e = n
while s<=e:
    mid = (s+e)//2
    if (mid+1) * (n-mid+1) > k:
        e = mid - 1
    elif (mid+1) * (n-mid+1) < k:
        s = mid + 1
    else:
        answer = True
        break

if answer:
    print('YES')
else:
    print('NO')