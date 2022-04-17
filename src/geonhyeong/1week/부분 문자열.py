# 부분 문자열.py
# Question Link: https://www.acmicpc.net/problem/16916
# Primary idea:     String
#                   1. 'in' 연산자를 이용하여 포함관계인지 확인
# 
# Time Complexity : O(n)
# Space Complexity : O(1)
# Runtime: 88 ms
# Memory Usage: 33.76 MB

S = input()
P = input()

print(1 if P in S else 0)