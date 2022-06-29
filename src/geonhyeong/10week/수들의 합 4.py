# 수들의 합 4.py
# Question Link: https://www.acmicpc.net/problem/2015
# Primary idea:     누적 합
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 240 ms
# Memory Usage: 45.904 MB

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = [0] + list(map(int, input().split())) # 입력받은 수들을 저장

prefix = [0] # 누적합을 저장할 리스트

# 누적
for i in range(1, n + 1):
    prefix.append(prefix[i - 1] + nums[i])

print(prefix) # [0, 2, 0, 2, 0]
cnt = {}
ans = 0

for i in range(n + 1):
    # (구하고자 하는 누적합) = (현재 누적합) - (이전의 어떤 누적합) = K
    ans += cnt.get(prefix[i] - k, 0)

    cnt[prefix[i]] = cnt.get(prefix[i], 0) + 1

print(ans)