#2800 괄호제거
#스택 이용: ( -> ), 인덱스 저장
from copy import deepcopy
from itertools import combinations

str = list(input())

bracket_index = []
bracket_tuple= []
answer = set() #(((1))) 와 같이 한쌍을 제거해도 같은 결과가 나오는 경우도 있음 -> set으로 중복 제거

for i in range(len(str)):
    if str[i] == "(":
        bracket_index.append(i) #인덱스 집어 넣음
    elif str[i] == ")": #닫는 표시 나온다면
        if (str[bracket_index[-1]] == "("):
            bracket_start = bracket_index.pop()
            bracket_tuple.append((bracket_start, i))

for i in range(1, len(bracket_tuple)+1): #조합 개수 반복문
    for combination in combinations(bracket_tuple,i):
        result_str = deepcopy(str)
        for j in combination:
            start, end = j
            result_str[start] = ""
            result_str[end] = ""
        answer.add("".join(result_str))

answer = sorted(answer)
for i in answer:
    print(i)