# 블로그2.py
# Question Link: https://www.acmicpc.net/problem/20365
# Primary idea:     그리디
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 200 ms
# Memory Usage: 31.328 MB

import sys
input = sys.stdin.readline

n = int(input())
str = input()

dict = { 'B' : 0, 'R' : 0 }

dict[str[0]] += 1 # 처음 색깔

for i in range(1, n): 
    if str[i] != str[i - 1]: # 다른 색이 나오면 
        dict[str[i]] += 1 # 해당 색깔 칠하는 횟수 + 1

# BB R B R BB R
# print(dict) # {'B': 3, 'R': 3}
result = min(dict['B'], dict['R']) + 1 # 칠할 횟수가 더 많은 것을 먼저 전체 칠하고(+1) 칠할 횟수가 더 적은 것의 횟수 값(min)을 더한다.
print(result)