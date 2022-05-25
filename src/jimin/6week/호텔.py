#1106 호텔
import sys
import math
input = sys.stdin.readline

c, n = map(int, input().split()) #늘릴 고객 수, 도시의 개수

dp_list = [math.inf] * (1101)
for i in range(n):
    cost, customer = map(int, input().split())
    dp_list[customer] = min(cost, dp_list[customer])

#들이는 돈의 최솟값 구하기
def dp():
    global dp_list
    for i in range(1, 1101):
        for j in range(1, i//2+1):
            dp_list[i] = min(dp_list[j]+dp_list[i-j], dp_list[i])

    return min(dp_list[c:])

print(dp())