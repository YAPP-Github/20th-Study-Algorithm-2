n, k = map(int, input().split())
seq = list(map(int, input().split()))

count = [0 for _ in range(100001)]
l = 0
answer = 0
for r in range(n):
    count[seq[r]] += 1
    if count[seq[r]] == k+1:
        answer = max(answer, r-l)
        while count[seq[r]] == k+1:
            count[seq[l]] -= 1
            l += 1
    else:
        answer = max(answer, r-l+1)
print(answer)