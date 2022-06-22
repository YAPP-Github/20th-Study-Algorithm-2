# 행복 유치원.py
# Question Link: https://www.acmicpc.net/problem/13164
# Primary idea:     그리디
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

import sys
input = sys.stdin.readline

# 입력
n, k = map(int, input().split())
kids = list(map(int, input().split()))

diff = []
for i in range(1, len(kids)):
    diff.append(kids[i] - kids[i - 1])

print(diff)
diff.sort(reverse = True)
print(diff)

print(diff[k - 1:])
print(sum(diff[k - 1:]))