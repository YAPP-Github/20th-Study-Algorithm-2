sticker = [14, 6, 5, 11, 3, 9, 2, 10]
#sticker = [1, 3, 2, 5, 4]
def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]
    elif n == 2:
        return max(sticker[0], sticker[1])
    dp1 = [0] * n
    #처음 스티커를 떼는 경우, 마지막 제외
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-2] + sticker[i], dp1[i-1])

    #두 번째부터 떼는 경우
    dp2 = [0] * n
    dp2[1] = sticker[1]
    for i in range(2,n):
        dp2[i] = max(dp2[i-2] + sticker[i], dp2[i-1])

    return max(max(dp1), max(dp2))

print(solution(sticker))