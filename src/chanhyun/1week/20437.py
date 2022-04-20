# Sling Window

t = int(input())
for _ in range(t):
    w = input()
    k = int(input())

    pos = [[] for _ in range(26)]
    for i in range(len(w)):
        pos[ord(w[i])-ord('a')].append(i)

    q3 = 10001
    q4 = -1
    for p in pos:
        for i in range(len(p)-k+1):
            q3 = min(q3, p[i+k-1] - p[i] + 1)
            q4 = max(q4, p[i+k-1] - p[i] + 1)
    
    if q3 == 10001 or q4 == -1:
        print(-1)
    else:
        print(q3, q4)
