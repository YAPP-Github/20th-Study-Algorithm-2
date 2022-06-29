# 후보 추천하기.py
# Question Link: https://www.acmicpc.net/problem/1713
# Primary idea:     시뮬레이션
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime: 72 ms
# Memory Usage: 30.840 MB

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
students = list(map(int, input().split()))
# key: 후보자번호
# value: [0]: 표갯수, [1]: 후보자 순서
photo = dict() # 사진틀, 

for i in range(m):
    if students[i] in photo:    # 사진틀에 O
        photo[students[i]][0] += 1

    else:                       # 사진틀에 X
        if len(photo) == n:     # 사진틀 꽉 차있으면
            del photo[students[sorted(photo.values())[0][1]]]

        photo[students[i]] = [1, i] # 1표, 후보자 순서

print(' '.join(map(str, sorted(photo.keys()))))