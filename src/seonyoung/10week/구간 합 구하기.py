n,m = map(int,input().split())

#1개씩 큰 배열로 만드러주기
numList = [[0] * (n + 1)]
for i in range (n):
    numList.append([0] + [int(temp) for temp in input().split()])

#행들끼리 합
for i in range (1,n+1):
    for j in range(1,n):
        numList[i][j+1] +=numList[i][j]

#열들끼리 합
for i in range(1,n):
    for j in range(1,n+1):
        numList[i+1][j]+=numList[i][j]

    
for i in range (m):
    x1,y1,x2,y2 = map(int, input().split())
    print(numList[x2][y2] - numList[x1 - 1][y2] - numList[x2][y1 -1] + numList[x1 - 1][y1 - 1])
