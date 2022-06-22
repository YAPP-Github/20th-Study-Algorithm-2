import sys
input = sys.stdin.readline

n, k = map(int, input().split()) #원생의 수 n, 나누고자 하는 조
arr = list(map(int,input().split()))

diff = []
for i in range(1, len(arr)):
    diff.append(arr[i]- arr[i-1])

diff.sort(reverse=True)
print(sum(diff[k-1:]))