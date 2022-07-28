# 달력.py
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

N = int(input())
calendar = [0] * 367
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    calendar[s] += 1
    calendar[e+1] -= 1 # 나중에 개수를 세어주기 위해서 시작부분에 일정이 추가되면 더하기 1, 일정이 끝나면 (마지막 부분 + 1) 에는 -1
 
width = 0
height = 0
answer = 0

for i in range(1, 367):
    calendar[i] += calendar[i-1] # 일정이 지속되고 있으니까 앞에 것을 계속 더해줘야 높이가 구해진다

    if calendar[i] == 0: # 일정이 없으면 이전에 있던 것의 너비를 하나 더해주고 아래에서 초기화
        answer += width * height
        width = 0
        height = 0
    else:
        width += 1
        height = max(height, calendar[i])
 
print(answer)