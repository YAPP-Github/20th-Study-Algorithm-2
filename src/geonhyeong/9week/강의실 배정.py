# 강의실 배정.py
# Question Link: https://www.acmicpc.net/problem/11000
# Primary idea:     그리디
#                   1. 강의실이 추가로 필요한 상황은 어떤 한 강의가 끝나지 않았는데 다른 강의가 시작하는 것
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 432 ms
# Memory Usage: 73.168 MB

import sys
import heapq
input = sys.stdin.readline

# 입력
n = int(input())

# 강의 입력
lecture = [list(map(int, input().split())) for _ in range(n)]
lecture.sort() # S(시작)을 기준으로 정렬

queue = [] 
heapq.heappush(queue, lecture[0][1]) # 첫 번째 강의가 끝나는 시간

for i in range(1, n):
    if lecture[i][0] < queue[0]: # 강의 시작시간 < 우선순위 큐의 첫 번째 인덱스
        heapq.heappush(queue, lecture[i][1]) # 해당 강의의 끝나는 시간
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, lecture[i][1]) # 해당 강의의 끝나는 시간

print(len(queue))