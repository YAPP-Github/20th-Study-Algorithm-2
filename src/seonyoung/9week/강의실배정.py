import heapq
#큐의 정렬상태 유지를 위한 우선순위 큐 사용

n = int(input())
classList = [list(map(int, input().split())) for _ in range(n)]
classList.sort()

classQueue = []
heapq.heappush(classQueue, classList[0][1]) #첫강의 종료

for i in range(1, n):
    if classList[i][0] < classQueue[0]:
        heapq.heappush(classQueue, classList[i][1])
    else:
        heapq.heappop(classQueue)
        heapq.heappush(classQueue, classList[i][1])

print(len(classQueue))