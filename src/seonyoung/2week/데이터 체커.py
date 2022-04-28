#모든 원의 중심 좌표는 x축 위에 존재해야 한다.
# N개의 원 중 임의의 두 원을 선택했을 때, 교점이 존재하지 않아야 한다. 
# 즉, 하나의 원이 다른 원 안에 존재하거나 외부에 존재한다.

#두 원이 만나지 않고, 두 점사이 거리가 둘의 반지름보다 클때!!

from ast import Return
from itertools import combinations
import math
checkFlag= True #하나로도 맞지않으면 false로 변경한 뒤에 리턴

def checking():
    n = int(input())
    circleList = []
    for i in range(n):
        x,r = map(int, input().split())
        circleList.append((x-r,i,0))
        circleList.append((x+r,i,1))

    circleList.sort()
    stackList=[]
    tempList= set()
    for bracket, i, flag in circleList:
        if bracket in tempList:
            #이미 있었다면(동심원)
            print('NO')
            return
        if flag==0:
            stackList.append((bracket,i))
        elif stackList[-1][1]!=i:
            # stack의 top의 index가 i가 아닐 경우 (원이 제대로 안닫힘=겹침)
            print('NO')
            return
        else:
            tempList.add(bracket)
            stackList.pop()
    print('YES')

if __name__=="__main__":
    checking()