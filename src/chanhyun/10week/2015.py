from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
for i in range(1, N):
    A[i] += A[i-1]

answer = 0
prefix_sum = defaultdict()
for i in range(N):
    if A[i] == K:
        answer += 1
    answer += prefix_sum[A[i]-K]
    prefix_sum[A[i]] += 1
print(answer)
