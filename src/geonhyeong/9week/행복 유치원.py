# 행복 유치원.py
# Question Link: https://www.acmicpc.net/problem/13164
# Primary idea:     그리디
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 296 ms
# Memory Usage: 64.404 MB

import sys
input = sys.stdin.readline

# 입력
n, k = map(int, input().split())
kids = list(map(int, input().split()))

diff = []
for i in range(1, len(kids)):
    diff.append(kids[i] - kids[i - 1]) # 키 차이

# print(diff) # [2, 2, 1, 4]
diff.sort(reverse = True)
# print(diff) # [4, 2, 2, 1]

# print(diff[k - 1:]) # k : 조 갯수
print(sum(diff[k - 1:]))