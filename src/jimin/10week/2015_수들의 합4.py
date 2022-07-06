#시간 초과
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = list(map(int,input().split()))

count = 0
prefix = [0]
pre_sum = 0
for i in range(len(arr)):
    pre_sum += arr[i]
    if(arr[i] == k):
        count += 1
    prefix.append(pre_sum)

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if (prefix[j]-prefix[i-1] == k):
            count += 1

print(count)