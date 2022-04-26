# 데이터 체커.py
# Question Link: https://www.acmicpc.net/problem/22942
# Primary idea:     자료구조, 정렬, stack
#                   1. 시간초과 때문에 sys를 이용
#                   2. x-r, x+r값을 저장
#                       2-1. [x-r or x+r, 시작인지 끝인지, 원의 번호]
#                   3. x축값의 거리순으로 정렬
#                   4. 원의 시작(1)이면 stack에 '원의 번호' 저장
#                   5. 원의 시작이 아니(0)라면 stack의 top과 같은지 비교후,
#                       5-1. 같으면 pop()
#                       5-2. 다르면 "NO"
#                       * top = stack[-1]
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 928 ms
# Memory Usage: 90.37 MB

import sys

circle = []
stack = [] # 원의 번호를 저장

# input
for i in range(int(input())):
    x, r = map(int, sys.stdin.readline().split(' ')) 
    circle.append([x-r, 1, i]) # 시작 x값, 시작 flag, 원의 번호
    circle.append([x+r, 0, i]) # 끝 x값, 끝 flag, 원의 번호

# sort
circle.sort()

for i in range(len(circle)):
    if circle[i][1]: # 원의 시작
        stack.append(circle[i][2])
    elif circle[i][2] == stack[-1]:
        stack.pop()
    else:
        print("NO")
        exit()

print("YES")
