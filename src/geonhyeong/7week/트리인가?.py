# .py
# Question Link: 
# Primary idea:     String
#                   1. 
# 
# Time Complexity : O()
# Space Complexity : O()
# Runtime:  ms
# Memory Usage:  MB

import sys
input = sys.stdin.readline

testCase = 1
node = set()
indegree = {}

def printRes(isTree):
    if isTree:
        print(f"Case {testCase} is a tree.")
    else:
        print(f"Case {testCase} is not a tree.")


while testCase:
    isTree = True           # Tree인지 아닌지 판별
    isNext = True           # 0 0이 들어올때까지
    cntEdge = 0             # edge의 갯수
    cntNode = 0             # Node의 갯수    
    node.clear()            # Tree 초기화
    indegree.clear()        # 들어오는 화살표 초기화

    while isNext:
        str = input().strip().split("  ")

        if str[0] == "":   # 공백일 경우
            continue

        if str[0] == "-1 -1":
            exit()

        for info in str:
            start, end = info[0], info[2]

            if start == '0' and end == '0':     # 0, 0일 경우
                isNext = False
                break
            
            cntEdge += 1                    # 간선 증가

            node.add(start)                 # Node 추가
            node.add(end)

            if end in indegree:             # 이미 들어오는 화살표가 있으면 not Tree
                isTree = False
            else:
                if start in indegree and indegree[start] == end: # cycle
                    isTree = False
                indegree[end] = start

    if cntEdge > 0 and len(node) != cntEdge + 1:
        isTree = False

    printRes(isTree)
    testCase += 1           # 다음 case
