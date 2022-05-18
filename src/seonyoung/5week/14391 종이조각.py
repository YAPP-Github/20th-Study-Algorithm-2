#비트마스크란?정수를 이진수 형태로 표현하여 자료구조로써 사용하는 기법
#a & b - 두 정수 a, b를 비트별로 AND 연산
#a | b - 두 정수 a, b를 비트별로 OR 연산
#a ^ b - 두 정수 a, b를 비트별로 XOR 연산
#~a - 정수 a의 비트열 NOT 언산 결과
#a << b - 정수 a를 왼쪽으로 b비트 시프트(왼쪽의 숫자를 연산 오른쪽 숫자 비트만큼 좌, 우로 이동하라는 의미)

n,m =map(int, input().split())
paper = [list(map(int,input())) for _ in range(n)]
answer=0

for case in range(1<<n*m):
    total = 0
    for row in range(n):
        rowSum =0 
        for col in range(m):
            index = row*m +col
            if case & (1<<index) !=0: #케이스가 존재하고 1을 index만큼 시프트 연산한게 0일경우
                rowSum = rowSum*10 +paper[row][col]
            else :
                total += rowSum
                rowSum =0
        total+=rowSum
    for col in range(m):
        colSum=0
        for row in range(n):
            index =row*m+col
            if case&(1<<index)==0:
                colSum=colSum*10+paper[row][col]
            else:
                total +=colSum
                colSum=0
        total +=colSum
    if(answer<total):
        answer=total
    

print(answer)