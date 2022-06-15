# 두 용액.py
# Question Link: https://www.acmicpc.net/problem/2470
# Primary idea:     투 포인터
#                   1. 아 완전탐색하고 싶다..
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 152 ms
# Memory Usage: 42.316 MB

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort() # 정렬, 오름차순 결과(결과값 저장할떄)
start, end = 0, len(arr) - 1

res = (arr[start], arr[end], abs(arr[start] + arr[end])) # 처음(가장 작은 값), 끝(가장 큰 값), abs(처음 + 끝)

while start < end:
    A, B = arr[start], arr[end] # A 용액, B 용액
    combine = abs(A + B)

    if combine < res[2]: # 최소값 저장
        res = (A, B, combine) # A, B도 값이 저장해놔야함

    if combine == 0: # 0이면 더이상 계산을 할 필요가 없다, 어차피 아무거나 출력
        break
    elif A + B < 0:
        start += 1
    else:
        end -= 1

print(res[0], res[1])