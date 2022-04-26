# 괄호 제거.py
# Question Link: https://www.acmicpc.net/problem/2800
# Primary idea:     자료구조, 문자열, 스택, 재귀
#                   1. 열린 괄호의 수에 따라 각각의 올바른 식을 구할까?
#                   2. 짝이 맞는 괄호의 index를 pairBracket에 저장
#                   3. 괄호의 pair에 따라 새로운 식을 만든 후, 반환하는 함수 선언
#                   4. combination으로 조합을 구한뒤, 새로운 식을 만듦
#                   5. '(((0)))'같은 hidden case를 고려해 res를 set으로 선언
# 
# Time Complexity : O() 
# Space Complexity : O()
# Runtime: 80 ms
# Memory Usage: 30.84 MB

from itertools import combinations

input = input()

res = set() # 결과 값
stack = [] # '('의 index를 저장하는 빈 스택(리스트) 초기화
pairBracket = [] # '('와 ')'의 index를 쌍으로 저장

# 짝이 맞는 괄호의 index를 pairBracket에 저장
for i in range(len(input)):
    if input[i] == '(':
        stack.append(i)
    elif input[i] == ')':
        open = stack.pop()
        pairBracket.append([open, i]) # 쌍으로 저장

# 괄호의 pair에 따라 새로운 식을 만든 후, 반환
def makeExpress(pair):
    new = ""
    for i, c in enumerate(input):
        if c == '(' or c == ')':
            if i in pair:
                new += c
        else:
            new += c
    return new

# combination으로 조합을 구한뒤, 새로운 식을 만듦
for i in range(len(pairBracket)):
    for pair in combinations(pairBracket, i):
        express = makeExpress(sum(pair, [])) # sum을 통해 2차원을 1차원 리스트로 변경
        res.add(express)

for express in sorted(res):
    print(express)