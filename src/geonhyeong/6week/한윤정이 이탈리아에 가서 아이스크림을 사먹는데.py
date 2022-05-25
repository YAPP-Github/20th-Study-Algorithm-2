# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데.py
# Question Link: https://www.acmicpc.net/problem/2422
# Primary idea:     완전탐색
#                   1. 3가지라고 할때, 3중 반복문이 떠오름
#                   2. 핵심은 '함꼐 먹으면 안되는 조합'을 제외 해야함
#                       1) 함께 먹으면 안되는 조합이 오름차순으로 들어온다는 보장이 없음 -> 양방향?으로 True로 설정해줘야함
#                       2) 미리 2중 배열을 선언해서 받는다
# 
# Time Complexity : O(n^3)
# Space Complexity : O(n^2)
# Runtime: 396 ms
# Memory Usage: 30.84 MB

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dont = [[False for _ in range(N+1)] for _ in range(N+1)] # 안되는 조합
for _ in range(M):
    taste1, taste2 = map(int, input().split())
    dont[taste1][taste2] = True
    dont[taste2][taste1] = True

res = 0 # 결과 갯수

for i in range(1, N+1):
    for j in range(i+1, N+1):
        for k in range(j+1, N+1):
            if not dont[i][j] and not dont[j][k] and not dont[i][k]:
                res += 1

print(res)