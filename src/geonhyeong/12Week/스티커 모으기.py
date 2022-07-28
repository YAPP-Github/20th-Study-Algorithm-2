# 스티커 모으기.py
# Question Link: 
# Primary idea:     String
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

def solution(sticker):

    n = len(sticker)

    if n <= 3:
        return max(sticker)

    dp1 = [0] * n
    dp2 = [0] * n

    dp1[0] = sticker[0] # 처음부터 시작, 맨 끝 제외
    dp1[1] = dp1[0]
    dp2[1] = sticker[1] # 처음의 다음부터 시작, 맨 끝 포함
    dp2[0] = 0

    for i in range(2, n-1):
        dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 1])

    for i in range(2, n):
        dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 1])

    return max(dp1[-2], dp2[-1])