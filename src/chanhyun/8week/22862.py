n, k = map(int, input().split())
s = list(map(int, input().split()))

answer = 0
odd = 0
even = 0
r = 0
for l in range(n):
    while odd <= k and r < n:
        if s[r] % 2 == 1:
            odd += 1
        else:
            even += 1
        r += 1

        if l == 0 and r == n:
            answer = even

    if odd == k+1:
        answer = max(answer, even)
    
    if s[l] % 2 == 1:
        odd -= 1
    else:
        even -= 1

print(answer)