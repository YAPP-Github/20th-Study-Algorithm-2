# 피아노 체조.py
# Question Link: https://www.acmicpc.net/problem/21318
# Primary idea:     누적 합
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 28 ms
# Memory Usage: 42.444 MB

import sys
input = sys.stdin.readline

n = int(input()) # 악보의 개수
score = list(map(int, input().split())) # 악보 난이도

 # 실수 누적합 구하기
missSum = [0] * n
for i in range(1, n):
    # 이전 악보가 현재 악보보다 난이도가 높은 경우 => 실수 발생 O
    if score[i - 1] > score[i]:
        missSum[i] = missSum[i - 1] + 1
    # 이전 악보가 현재 악보보다 난이도가 낮은 경우 => 실수 발생 X
    else :
        missSum[i] = missSum[i - 1]

Q = int(input()) # 질문의 개수

for _ in range(Q):
    x, y = map(int, input().split())
    # x번 부터 y번 악보까지 연주할 때, 발생하는 실수 개수 출력
    print(missSum[y - 1] - missSum[x - 1])