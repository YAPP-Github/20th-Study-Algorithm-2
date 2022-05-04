#https://www.acmicpc.net/problem/21939
#아직 보는 중입니다!!

from heapq import heappop, heappush

n = int(input())
testList = {} 
maxList = []
minList = []

for  i in range(n):
    number, level = map(int,input().split())
    heappush(minList,(level,number)) #오름차순
    heappush(maxList,(-level,-number)) #내림차순
    if not testList.get(number):
        testList[number]=0
    testList[number]=level


m = int(input())
for i in range(m):
    commandList = list(input().split())
    command = commandList[0]

    if command=='recommend':
        if commandList[1] == '1':
            #최대일 때 
            while maxList and testList[maxList[-1][1]]!=maxList[[0][0]]:
                heappop(maxList)
            print(maxList[0][1]) #문제번호 출력
        else:
            while minList and testList[minList[0][1]]!=minList[[0][0]]:
                heappop(minList)
            print(minList[0][1])
    elif command =='add':
        number, level = int(commandList[1]),int(commandList[2])
        heappush(minList,(level,number))
        heappush(maxList,(level,number))
        if not testList.get(number):
            testList[number]=0 
        testList[number]=level
    elif command=='solved':

        number = commandList[1]
        testList[number]=0
        pass


