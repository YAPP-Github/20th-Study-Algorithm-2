#1477
import sys
input = sys.stdin.readline

def binary_search(start, end):
    result = 0
    while (start <= end):
        cnt = 0
        mid = (start + end) // 2
        for i in range(1, len(locates)):
            dist = locates[i] - locates[i-1]
            if (dist > mid):
                cnt += (dist-1) // mid

        if cnt > m:
            start = mid + 1
        else:
            end = mid - 1
            result = mid
    return result

n, m, l = map(int, input().split()) #현재 휴게소, 더 세울 것, 고속도로 길이
locates = list(map(int, input().split()))
locates.append(l)
locates.append(0)
locates = sorted(locates)

print(binary_search(1, locates[-1]))
