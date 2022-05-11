# https://www.acmicpc.net/problem/19637

n,m=map(int,input().split())
powerList =[]
powerNameList = []


def binarySearch(p):
    left, right = 0, len(powerList)-1
    while left<=right:
        mid = (left+right)//2
        if p> powerList[mid]:
            left = mid+1
        else :
            right=mid-1
    print(powerNameList[right+1])


for i in range(n):
    name,power =input().split()
    if powerList and  powerList[-1] ==power:
        continue
    powerList.append(int(power))
    powerNameList.append(name)


for i in range(m):
    temp = int(input())
    binarySearch(temp)