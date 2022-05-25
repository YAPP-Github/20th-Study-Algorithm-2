#14391 종이 조각
#세로 가로 구분 필요 -> 0 or 1
#스터디 진행 후 코드 참고해서 풀어보았습니다!!!
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int,input().strip())) for _ in range(n)]

answer = 0
for case in range(1<<n*m):
    temp = 0
    for i in range(n):
        temp_row = 0
        for j in range(m):
            num = m * i + j
            if (case & 1<<num) != 0: #case에서 num 일 때 포함되어 있는지 and 연산으로 확인
                temp_row = temp_row*10 + arr[i][j]
            else:
                temp += temp_row
                temp_row = 0
        temp += temp_row

    for j in range(m):
        temp_column = 0
        for i in range(n):
            num = m * i + j
            if (case & 1<< num) == 0:
                temp_column =temp_column * 10 + arr[i][j]
            else:
                temp += temp_column
                temp_column = 0
        temp += temp_column
    answer = max(answer, temp)

print(answer)