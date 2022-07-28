# 입국심사.py
# Question Link: https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=python3
# Primary idea:     이분 탐색
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

import sys
input = sys.stdin.readline

def solution(n, times):
    answer = 0

    left = 1      
    right = max(times) * n  # 가장 긴 심사시간이 소요되는 심사관에게 n 명 모두 심사받는 경우

    while left <= right:
        mid = (left + right) // 2
        people = 0 # 심사한 사람의 수

        for time in times:
            people += mid // time # 모든 심사관들이 mid분 동안 심사한 사람의 수
            
            if people >= n: # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수
                break

        if people >= n: # n :심사 받아야할 사람의 수
            answer = mid
            right = mid - 1
        elif people < n:
            left = mid + 1
            
    return answer