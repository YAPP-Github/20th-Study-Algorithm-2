#2156 포도주 시식

#포도잔을 선택하면 모두 마셔야 함, 마신 후에 원래 다리에 놓아야 함
#3잔을 모두 마실 수는 없다
#3번째일 때 1+2(이전 값) or 1+3 큰 값 저장 즉, arr[i-2] + arr[i], arr[i-1] max ..
#4번째일 때 1+2+4 or 2+3 (이전까지 합) or 1+3+4

import sys
input = sys.stdin.readline

n = int(input()) #포도잔의 개수
arr = [0]
for i in range(n):
    arr.append(int(input()))

dp_list = [0]
def dp():
    if (n == 1):
        return arr[1]
    elif (n==2):
        return arr[1]+arr[2]
    elif (n > 2):
        dp_list.append(arr[1])
        dp_list.append(arr[1] + arr[2])
    for i in range(3, n+1):
        dp_list.append(max(dp_list[i-1], dp_list[i-2]+ arr[i], arr[i-1]+arr[i]+dp_list[i-3]))
    return dp_list[-1]

print(dp())
