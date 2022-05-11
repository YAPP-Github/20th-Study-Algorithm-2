#20444 색종이와 가위

#1. 한 변에 평행하게 자른다.
#2. 경로 상의 모든 색종이를 자를 때까지 멈추지 않는다.
#3. 이미 자른 곳을 또 자를 수 없다.

#n 번 가위 질로 k개의 색종이 조각을 만들 수 있는가?
# k = (세로 + 1) * ((n-세로)+1)

import sys
input = sys.stdin.readline
n, k = map(int, input().split())

def binarySearch(start, end):
    while (start <= end):
        col = (start + end) // 2
        row = n - col
        paper_cnt = (col + 1) * (row +1)
        if paper_cnt == k:
            return 'YES'
        elif paper_cnt > k :
            end = col -1
        else:
            start = col + 1
    return 'NO'

print(binarySearch(0, n//2))