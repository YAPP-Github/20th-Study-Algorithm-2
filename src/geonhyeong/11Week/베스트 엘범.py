# 베스트엘범.py
# Question Link: https://school.programmers.co.kr/learn/courses/30/lessons/42579
# Primary idea:     해쉬
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

import sys
input = sys.stdin.readline

def solution(genres, plays):
    dic = {}
    
    for (i, genre) in enumerate(genres):
        if genre in dic.keys():
            dic[genre].append((plays[i], i))
        else:
            dic[genre] = [(plays[i], i)]

    # 장르 내에서 많이 재생된 노래를 먼저 수록
    for key, value in dic.items():
        dic[key].sort(key=lambda x : (-x[0], x[1]))

    sumList = []
    # print(dic)
    for key in dic.keys():
        sumvalue = 0
        for play, priority in dic[key]:
            sumvalue += play
        sumList.append((sumvalue, key))

    # 속한 노래가 많이 재생된 장르를 먼저 수록
    sumList.sort(key=lambda x: -x[0])
    # print(sumList)
    res = [] 
    for total, genre in sumList:
        for play, priority in dic[genre][:2]:
            res.append(priority)

    return res