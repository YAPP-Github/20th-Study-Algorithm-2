# 트리.py
# Question Link: 
# Primary idea:     String
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

import sys
input = sys.stdin.readline

def dfs(num, arr):
    arr[num] = -2 # 삭제될 노드들은 전부 -2로 초기화
    
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)

# 입력
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

dfs(k, arr)

cnt = 0
for i in range(len(arr)): 
    if arr[i] != -2 and i not in arr:
        cnt += 1

print(cnt)