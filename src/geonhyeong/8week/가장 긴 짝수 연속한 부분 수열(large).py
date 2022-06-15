# 가장 긴 짝수 연속한 부분 수열(large).py
# Question Link: https://www.acmicpc.net/problem/22862
# Primary idea:     투 포인터
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 1216 ms
# Memory Usage: 149.420 MB

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
res = 0 if arr[start] % 2 != 0 else 1
cntOdd = 1 if arr[start] % 2 != 0 else 0 # 홀수 개수

while end < n-1:
    end += 1 # end를 한칸 오른쪽으로 옮긴다

    # 옮긴곳이 홀수이면, cntOdd += 1
    if arr[end] % 2 != 0:
        cntOdd += 1 

        # 범위내의 홀수의 개수가 K보다 크다면,
        while cntOdd > k: # 홀수가 하나 빠질때까지 start 포인터를 +1 
            if arr[start] % 2 != 0:
                cntOdd -= 1
            start += 1

    res = max(res, end - start + 1 - cntOdd)

print(res)