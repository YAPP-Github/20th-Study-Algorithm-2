import sys
input = sys.stdin.readline

def string_game(w,k):
    min_len = float("inf")
    max_len = float("-inf")
    len_w = len(w)
    if k == 1:
        return [1, 1]

    alphabet = [0]*26
    for i in w:
        if alphabet[ord(i)-ord('a')] == 0:
            alphabet[ord(i)-ord('a')]= w.count(i)

    flag = False
    for i in range(len_w):
        if (alphabet[ord(w[i])-97]< k): #시간 초과 막기 위해서 미리 개수 계산 후 진행 
            continue
        count = 1
        for j in range(i+1, len_w):
            if(w[i] == w[j]):
                count +=1
            if (count == k):
                min_len = min(min_len, j-i+1)
                max_len = max(max_len, j-i+1)
                flag = True
                break
    if not flag:
        return [-1]
    else:
        return [min_len, max_len]

t = int(input())
for i in range(t):
    w = input().rstrip()
    k = int(input().rstrip())
    print(*string_game(w,k))
