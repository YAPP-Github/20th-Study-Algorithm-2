n, k = map(int, input().split())
childList = list(map(int, input().split()))
diffList = []

for i in range(1, n):
    diffList.append(childList[i] - childList[i-1])
diffList.sort(reverse=True)

print(sum(diffList[k-1:]))