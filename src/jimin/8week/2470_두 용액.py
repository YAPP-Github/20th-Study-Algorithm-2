#2470 두 용액
#두 용액을 섞어 0에 가장 가까운 욕액

import sys
import math
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
sort = arr.sort()

left, right = 0, n-1
answer_left, answer_right = 0, 0
answer = math.inf
while(left < right):
    temp_sum = arr[left] + arr[right]

    if abs(temp_sum) < answer:
        answer = abs(temp_sum)
        answer_left, answer_right = left, right

    if temp_sum < 0:
        left += 1
    else:
        right -= 1

print(arr[answer_left], arr[answer_right])
