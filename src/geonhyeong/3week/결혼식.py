# 결혼식.py
# Question Link: https://www.acmicpc.net/problem/5567
# Primary idea:     그래프 이론, 그래프 탐색
#                   1. dictionary을 list([]) 초기화
#                   2. dictionary로 관계를 '양방향'으로 넣어주기
#                   3. relation[1]이 존재 할 경우,
#                       1) set으로 relation[1]을 포함 후, 자기자신(1)을 제외한 후 길이 출력
#                   4. relation[1]이 []일 경우,
#                       1) 0 출력
# 
# Time Complexity : O(n)
# Space Complexity : O(n)
# Runtime: 80 ms
# Memory Usage: 30.84 MB

import sys
input = sys.stdin.readline

n = int(input())
relation = dict()

# 초기화
for i in range(1, n+1):
    relation[i] = []

# 입력
for _ in range(int(input())):
    friend1, friend2 = map(int, input().split(' '))

    # 양방향
    relation[friend1].append(friend2)
    relation[friend2].append(friend1)

# 찾기
if relation[1]:
    res = set(relation[1])
    for i in relation[1]:
        res.update(relation[i]) 
    print(len(res) - 1) # 본인 제외
else:
    print(0)