
# 단어 뒤집기 2.py
# Question Link: https://www.acmicpc.net/problem/17413
# Primary idea:     <String>
#                   1. 처음에는 split으로 해결하려고 함.
#                   2. Flag를 이용해서 Tag가 시작되는지를 판별
#                   3. 정상 출력(Falg == True)일때,
#                       1) 결과값(res)에 그대로 붙임
#                       2) '>'일떄(Tag가 끝), Flag = False
#                   4. 뒤집어 출력(Flag == False)일때,
#                       1) '<'일때(Tag가 시작)
#                           a) Falg = True
#                           b) 모아놓은 단어(word)와 '<'를 붙인 후
#                           c) word 초기화
#                       2) ' '(공백)일때,
#                           a) 모아놓은 단어(word)와 ' '를 붙인 후
#                           c) word 초기화
#                       3) word의 앞에 붙여서 reverse된 단어(word)를 모으기
# 
# Time Complexity : O(n)
# Space Complexity : O(1)
# Runtime: 304 ms
# Memory Usage: 30.84 MB

sentence = input()

res = ""        # 결과
flag = False    # Tag의 단어인지 판별, True = tag시작
word = ""       # 뒤집어야할 단어

for c in sentence:
    # 정상 출력
    if flag:
        res += c
        if c == '>':
            flag = False

    # 뒤집어 출력
    else:
        if c == '<':
            flag = True
            res += word + '<'
            word = ''
        elif c == ' ':
            res += word + ' '
            word = ""
        else:
            word = c + word

print(res + word)