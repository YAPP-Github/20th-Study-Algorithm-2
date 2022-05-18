# 도영이가 만든 맛있는 음식.py
# Question Link: https://www.acmicpc.net/problem/2961
# Primary idea:     완전탐색
#                   1. 모든 조합(dfs) 문제라고 생각했다
# 
# Time Complexity : O(n!)
# Space Complexity : O(n)
# Runtime: 68 ms
# Memory Usage: 30.84 MB

import sys
input = sys.stdin.readline

N = int(input())

taste = [] # 신맛, 쓴맛 저장
for _ in range(N):
    sour, bitter = map(int, input().split()) # 신맛, 쓴맛
    taste.append([sour, bitter])

isVisited = [False for _ in range(N)]

minValue = float('inf')

def dfs(j, sumS, sumB):
    global minValue

    if j == N:
        return 

    for i in range(j, N):
        if not isVisited[i]:
            isVisited[i] = True
            minValue = min(minValue, abs(sumS * taste[i][0] - (sumB + taste[i][1])))
            dfs(i+1, sumS * taste[i][0], sumB + taste[i][1])
            isVisited[i] = False

dfs(0, 1, 0)
print(minValue)