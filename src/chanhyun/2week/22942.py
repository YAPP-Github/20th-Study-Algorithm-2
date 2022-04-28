n = int(input())
points = []
for i in range(n):
    x, r = map(int, input().split())
    points.append((x-r, 0, i))
    points.append((x+r, 1, i))
points.sort()

answer = True
right = []
while points:
    c = points.pop()
    if c[1] == 1:
        right.append(c)
    else:
        if right == []:
            answer = False
            break
        else:
            if c[2] != right[-1][2]:
                answer = False
                break
            else:
                right.pop()
    if points and c[0] == points[-1][0]:
        answer = False
        break

if answer:
    print("YES")
else:
    print("NO")