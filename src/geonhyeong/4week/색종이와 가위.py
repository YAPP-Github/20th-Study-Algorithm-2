# 색종이와 가위.py
# Question Link: https://www.acmicpc.net/problem/20444
# Primary idea:     이분 탐색, 수학
#                   1. 수학적 개념 - (row+1)*(col+1) = K 
#                       1) row : 가로로 자른 횟수
#                       2) col : 세로로 자른 횟수
#                   2. 왜 0~N까지 검사하지않고 0~N//2까지만 해도 되는지?
#                       1) 총 횟수(n)가 정해져 있기 때문에 가로+세로가 일정하다.
#                       2) 가로랑 세로의 결과가 같으므로 (가로, 세로)횟수가 대칭일 경우 같은 조각개수가 나온다 
#                       ex) 가로1+세로9 = 가로9+세로1
# 
# Time Complexity : O(logN)
# Space Complexity : O()
# Runtime: 76 ms
# Memory Usage: 30.84 MB

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
left, right = 0, n//2

while left <= right:
    row = (left + right) // 2   # 가로
    col = n - row               # 세로
    area = (row+1) * (col+1)
    print(row, col, area, k)
    if area < k:
        left = row + 1
    elif area > k:
        right = row - 1
    else:
        print("YES")
        exit()

print("NO")