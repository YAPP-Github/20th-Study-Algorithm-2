import sys
import heapq
input = sys.stdin.readline

n = int(input())
lectures = [list(map(int,input().split())) for _ in range(n)]

lectures = sorted(lectures, key= lambda x:x[0]) #시작시간 기준 정렬
end_time = [0]
for lecture in lectures:
    if end_time[0] <= lecture[0]:
        heapq.heappop(end_time)
    heapq.heappush(end_time, lecture[1])

print(len(end_time))
