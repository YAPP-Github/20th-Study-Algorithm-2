n, k = map(int, input().split())
score = list(map(int, input().split()))

answer = 0
l = 0
r = 10**5*20
while l<=r:
    mid = (l+r)//2
    group = 0
    g_score = 0
    for s in score:
        g_score += s
        if g_score >= mid:
            group += 1
            g_score = 0
    if group >= k:
        answer = mid
        l = mid+1
    else:
        r = mid-1
        
print(answer)