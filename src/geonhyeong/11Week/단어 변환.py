# 단어 변환.py
# Question Link: https://school.programmers.co.kr/learn/courses/30/lessons/43163
# Primary idea:     DFS/BFS
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

from collections import deque

def solution(begin, target, words):
    q = deque()
    q.append([begin, 0])

    arr = [ 0 for i in range(len(words))]

    while q:
        word, cnt = q.popleft()

        if word == target:
            return cnt

        for i in range(len(words)):
            diff = 0 # 다른 단어의 글자 수

            if not arr[i]: 
                for j in range(len(word)): # 다른 단어가 몇개가 같은지
                    if word[j] != words[i][j]:
                        diff += 1

                if diff == 1: # 단어가 1글자만 다를때
                    q.append([words[i], cnt + 1])
                    arr[i] = 1
                    
    return 0