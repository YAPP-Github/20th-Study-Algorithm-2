import sys
from collections import deque
input = sys.stdin.readline

#불행도 합 최소, 불행도: 샘터와의 거리

n, k = map(int,input().split()) #샘터, 집 수
site = list(map(int,input().split())) #샘터 위치
dx = [-1, 1]
results = dict() #집 위치: 거리로 저장

def bfs(site):
    queue = deque()
    for i in site:
        queue.append(i)
        results[i] = 0
    house_cnt = 0
    while(queue or house_cnt < k):
        x = queue.popleft()
        for i in range(2):
            nx = x + dx[i]
            if not nx in results.keys() and house_cnt < k:
                results[nx] = results[x] + 1 #거리 증가
                queue.append(nx)
                house_cnt += 1

bfs(site)
result_sum = 0
for i in results.values():
    result_sum += i

print(result_sum)

