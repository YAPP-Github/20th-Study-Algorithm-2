#1715 카드 정렬하기
import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = list(int(input()) for i in range(n))

def count():
    if n == 1:
        return 0
    answer = 0
    heapq.heapify(arr)
    while(len(arr) != 1):
        temp = heapq.heappop(arr) + heapq.heappop(arr)
        answer += temp
        heapq.heappush(arr, temp)
    return answer

print(count())
