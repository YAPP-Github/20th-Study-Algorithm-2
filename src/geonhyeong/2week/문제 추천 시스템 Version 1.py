# 문제 추천 시스템 Version 1.py
# Question Link: https://www.acmicpc.net/problem/21939
# Primary idea:     자료구조, 우선순위 큐
#                   1. 
# 
# Time Complexity : O(log n)
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

import sys
from heapq import heappop, heappush

# func add
def add(P, L):
    isSolved[P] = False
    heappush(minHeap, (L, P)) # L(문제 난이도)를 기준으로 최소 heap
    heappush(maxHeap, (-L, -P)) # L(문제 난이도)를 기준으로 최대 heap

# func solved
def solved(P):
    isSolved[P] = True
    while isSolved[-maxHeap[0][1]]:
        heappop(maxHeap)
    while isSolved[minHeap[0][1]]:
        heappop(minHeap) 

# func recommend
def recommend(type):
    if type == "1":
        while isSolved[-maxHeap[0][1]]:
            heappop(maxHeap)
        print(-maxHeap[0][1])
    elif type == "-1":
        while isSolved[minHeap[0][1]]:
            heappop(minHeap)
        print(minHeap[0][1])

# 선언
minHeap = [] # heap(최대)
maxHeap = [] # heap(최대)
isSolved = dict()

# heap insert
for _ in range(int(input())):
    P, L = map(int, sys.stdin.readline().split(' '))
    add(P, L)

# solution
for _ in range(int(input())):
    command = sys.stdin.readline().strip().split(' ')
    
    if command[0] == 'add': # add
        add(int(command[1]), int(command[2]))
    elif command[0] == 'solved': # solved
        solved(int(command[1]))
    elif command[0] == 'recommend': # recommend
        recommend(command[1])